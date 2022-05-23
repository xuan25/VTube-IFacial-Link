
import threading

import wx

import ifacial
from models import CapturedData


class ParamsFrame(wx.Frame):
    def __init__(self, capture_data: CapturedData):
        super().__init__(None, wx.ID_ANY, "VTube-IFacial-Link")
        self.capture_data = capture_data
        self.create_ui()
        self.Bind(wx.EVT_CLOSE, self.on_close)

        self.capture_timer = wx.Timer(self, wx.ID_ANY)
        self.Bind(wx.EVT_TIMER, self.update_capture_panel,
                  id=self.capture_timer.GetId())

        self.last_pose = None

        self.capture_timer.Start(33)

    def on_close(self, event: wx.Event):
        self.capture_timer.Stop()
        event.Skip()

    def create_ui(self):
        self.main_sizer = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(self.main_sizer)
        self.SetAutoLayout(1)

        self.capture_pose_lock = threading.Lock()

        self.create_capture_panel(self)
        self.main_sizer.Add(self.capture_panel, wx.SizerFlags(
            0).Expand().Border(wx.ALL, 5))

        self.main_sizer.Fit(self)

    def create_capture_panel(self, parent):
        self.capture_panel = wx.Panel(parent, style=wx.RAISED_BORDER)
        self.capture_panel_sizer = wx.FlexGridSizer(cols=5)
        for i in range(5):
            self.capture_panel_sizer.AddGrowableCol(i)
        self.capture_panel.SetSizer(self.capture_panel_sizer)
        self.capture_panel.SetAutoLayout(1)

        self.blendshape_labels = {}
        self.blendshape_value_labels = {}
        self.blendshape_gauges = {}
        blendshape_column_0 = self.create_blendshapes_column(
            self.capture_panel, ifacial.COLUMN_0_BLENDSHAPES)
        self.capture_panel_sizer.Add(
            blendshape_column_0, wx.SizerFlags(0).Expand().Border(wx.ALL, 3))
        blendshape_column_1 = self.create_blendshapes_column(
            self.capture_panel, ifacial.COLUMN_1_BLENDSHAPES)
        self.capture_panel_sizer.Add(
            blendshape_column_1, wx.SizerFlags(0).Expand().Border(wx.ALL, 3))
        blendshape_column_2 = self.create_blendshapes_column(
            self.capture_panel, ifacial.COLUMN_2_BLENDSHAPES)
        self.capture_panel_sizer.Add(
            blendshape_column_2, wx.SizerFlags(0).Expand().Border(wx.ALL, 3))
        blendshape_column_3 = self.create_blendshapes_column(
            self.capture_panel, ifacial.COLUMN_3_BLENDSHAPES)
        self.capture_panel_sizer.Add(
            blendshape_column_3, wx.SizerFlags(0).Expand().Border(wx.ALL, 3))
        blendshape_column_4 = self.create_blendshapes_column(
            self.capture_panel, ifacial.COLUMN_4_BLENDSHAPES)
        self.capture_panel_sizer.Add(
            blendshape_column_4, wx.SizerFlags(0).Expand().Border(wx.ALL, 3))

        self.rotation_labels = {}
        self.rotation_position_value_labels = {}
        rotation_column_0 = self.create_rotation_position_column(
            self.capture_panel, ifacial.RIGHT_EYE_ROTATIONS)
        self.capture_panel_sizer.Add(
            rotation_column_0, wx.SizerFlags(0).Expand().Border(wx.ALL, 4))
        rotation_column_1 = self.create_rotation_position_column(
            self.capture_panel, ifacial.LEFT_EYE_ROTATIONS)
        self.capture_panel_sizer.Add(
            rotation_column_1, wx.SizerFlags(0).Expand().Border(wx.ALL, 4))
        rotation_column_2 = self.create_rotation_position_column(
            self.capture_panel, ifacial.HEAD_ROTATIONS)
        self.capture_panel_sizer.Add(
            rotation_column_2, wx.SizerFlags(0).Expand().Border(wx.ALL, 4))
        position_column_1 = self.create_rotation_position_column(
            self.capture_panel, ifacial.HEAD_POSITIONS)
        self.capture_panel_sizer.Add(
            position_column_1, wx.SizerFlags(0).Expand().Border(wx.ALL, 4))


    def create_blendshapes_column(self, parent, blendshape_names):
        column_panel = wx.Panel(parent, style=wx.SIMPLE_BORDER)
        column_panel_sizer = wx.FlexGridSizer(cols=3)
        column_panel_sizer.AddGrowableCol(1)
        column_panel.SetSizer(column_panel_sizer)
        column_panel.SetAutoLayout(1)

        for blendshape_name in blendshape_names:
            self.blendshape_labels[blendshape_name] = wx.StaticText(
                column_panel, label=blendshape_name, style=wx.ALIGN_RIGHT)
            column_panel_sizer.Add(self.blendshape_labels[blendshape_name],
                                   wx.SizerFlags(1).Expand().Border(wx.ALL, 3))

            self.blendshape_gauges[blendshape_name] = wx.Gauge(
                column_panel, style=wx.GA_HORIZONTAL, size=(100, -1))
            column_panel_sizer.Add(self.blendshape_gauges[blendshape_name], wx.SizerFlags(
                1).Expand().Border(wx.ALL, 3))

            self.blendshape_value_labels[blendshape_name] = wx.TextCtrl(
                column_panel, style=wx.TE_RIGHT, size=(40, -1))
            self.blendshape_value_labels[blendshape_name].SetValue("0.00")
            self.blendshape_value_labels[blendshape_name].Disable()
            column_panel_sizer.Add(self.blendshape_value_labels[blendshape_name],
                                   wx.SizerFlags(0).Border(wx.ALL, 3))

        column_panel.GetSizer().Fit(column_panel)
        return column_panel

    def create_rotation_position_column(self, parent, rotation_names):
        column_panel = wx.Panel(parent, style=wx.SIMPLE_BORDER)
        column_panel_sizer = wx.FlexGridSizer(cols=2)
        column_panel_sizer.AddGrowableCol(1)
        column_panel.SetSizer(column_panel_sizer)
        column_panel.SetAutoLayout(1)

        for rotation_position_name in rotation_names:
            self.rotation_labels[rotation_position_name] = wx.StaticText(
                column_panel, label=rotation_position_name, style=wx.ALIGN_RIGHT)
            column_panel_sizer.Add(self.rotation_labels[rotation_position_name],
                                   wx.SizerFlags(1).Expand().Border(wx.ALL, 3))

            self.rotation_position_value_labels[rotation_position_name] = wx.TextCtrl(
                column_panel, style=wx.TE_RIGHT)
            self.rotation_position_value_labels[rotation_position_name].SetValue("0.00")
            self.rotation_position_value_labels[rotation_position_name].Disable()
            column_panel_sizer.Add(self.rotation_position_value_labels[rotation_position_name],
                                   wx.SizerFlags(1).Expand().Border(wx.ALL, 3))

        column_panel.GetSizer().Fit(column_panel)
        return column_panel

    def paint_capture_panel(self, event: wx.Event):
        self.update_capture_panel(event)

    def update_capture_panel(self, event: wx.Event):
        data = self.capture_data.read_data()
        for blendshape_name in ifacial.BLENDSHAPE_NAMES:
            value = data[blendshape_name]
            self.blendshape_gauges[blendshape_name].SetValue(
                ParamsFrame.convert_to_100(value))
            self.blendshape_value_labels[blendshape_name].SetValue(
                "%0.2f" % value)
        for rotation_position_name in ifacial.ROTATION_POSITION_NAMES:
            value = data[rotation_position_name]
            self.rotation_position_value_labels[rotation_position_name].SetValue("%0.2f" % value)

    @staticmethod
    def convert_to_100(x):
        return int(max(0.0, min(1.0, x)) * 100)
