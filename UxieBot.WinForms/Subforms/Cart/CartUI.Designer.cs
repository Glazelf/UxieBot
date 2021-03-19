
namespace UxieBot.WinForms
{
    partial class CartUI
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.TextBoxIP = new System.Windows.Forms.TextBox();
            this.ButtonConnect = new System.Windows.Forms.Button();
            this.GroupSysBotConnection = new System.Windows.Forms.GroupBox();
            this.LabelPort = new System.Windows.Forms.Label();
            this.LabelIP = new System.Windows.Forms.Label();
            this.TextBoxPort = new System.Windows.Forms.TextBox();
            this.GroupSysBotStatus = new System.Windows.Forms.GroupBox();
            this.StatusConnection = new System.Windows.Forms.Label();
            this.StatusConnectionLabel = new System.Windows.Forms.Label();
            this.ButtonSysbotRead = new System.Windows.Forms.Button();
            this.SysBotTabControl = new System.Windows.Forms.TabControl();
            this.TabSysBot = new System.Windows.Forms.TabPage();
            this.TabSysBotLog = new System.Windows.Forms.TabPage();
            this.SysBotLog = new System.Windows.Forms.RichTextBox();
            this.GroupSysBotConnection.SuspendLayout();
            this.GroupSysBotStatus.SuspendLayout();
            this.SysBotTabControl.SuspendLayout();
            this.TabSysBotLog.SuspendLayout();
            this.SuspendLayout();
            // 
            // TextBoxIP
            // 
            this.TextBoxIP.AccessibleName = "TextBoxIP";
            this.TextBoxIP.Location = new System.Drawing.Point(44, 28);
            this.TextBoxIP.Name = "TextBoxIP";
            this.TextBoxIP.Size = new System.Drawing.Size(96, 20);
            this.TextBoxIP.TabIndex = 0;
            this.TextBoxIP.Text = "192.168.0.1";
            // 
            // ButtonConnect
            // 
            this.ButtonConnect.AccessibleName = "ButtonConnect";
            this.ButtonConnect.Location = new System.Drawing.Point(44, 81);
            this.ButtonConnect.Name = "ButtonConnect";
            this.ButtonConnect.Size = new System.Drawing.Size(84, 24);
            this.ButtonConnect.TabIndex = 2;
            this.ButtonConnect.Text = "Connect";
            this.ButtonConnect.UseVisualStyleBackColor = true;
            this.ButtonConnect.Click += new System.EventHandler(this.ButtonConnect_Click);
            // 
            // GroupSysBotConnection
            // 
            this.GroupSysBotConnection.AccessibleName = "GroupSysBotConnection";
            this.GroupSysBotConnection.Controls.Add(this.LabelPort);
            this.GroupSysBotConnection.Controls.Add(this.LabelIP);
            this.GroupSysBotConnection.Controls.Add(this.TextBoxPort);
            this.GroupSysBotConnection.Controls.Add(this.ButtonConnect);
            this.GroupSysBotConnection.Controls.Add(this.TextBoxIP);
            this.GroupSysBotConnection.Location = new System.Drawing.Point(370, 436);
            this.GroupSysBotConnection.Name = "GroupSysBotConnection";
            this.GroupSysBotConnection.Size = new System.Drawing.Size(163, 119);
            this.GroupSysBotConnection.TabIndex = 3;
            this.GroupSysBotConnection.TabStop = false;
            this.GroupSysBotConnection.Text = "Connection";
            // 
            // LabelPort
            // 
            this.LabelPort.AccessibleName = "LabelPort";
            this.LabelPort.AutoSize = true;
            this.LabelPort.Location = new System.Drawing.Point(9, 57);
            this.LabelPort.Name = "LabelPort";
            this.LabelPort.Size = new System.Drawing.Size(29, 13);
            this.LabelPort.TabIndex = 5;
            this.LabelPort.Text = "Port:";
            // 
            // LabelIP
            // 
            this.LabelIP.AccessibleName = "LabelIP";
            this.LabelIP.AutoSize = true;
            this.LabelIP.Location = new System.Drawing.Point(18, 31);
            this.LabelIP.Name = "LabelIP";
            this.LabelIP.Size = new System.Drawing.Size(20, 13);
            this.LabelIP.TabIndex = 4;
            this.LabelIP.Text = "IP:";
            // 
            // TextBoxPort
            // 
            this.TextBoxPort.AccessibleName = "TextBoxPort";
            this.TextBoxPort.Location = new System.Drawing.Point(44, 54);
            this.TextBoxPort.Name = "TextBoxPort";
            this.TextBoxPort.Size = new System.Drawing.Size(96, 20);
            this.TextBoxPort.TabIndex = 3;
            this.TextBoxPort.Text = "6000";
            // 
            // GroupSysBotStatus
            // 
            this.GroupSysBotStatus.AccessibleName = "GroupSysBotStatus";
            this.GroupSysBotStatus.Controls.Add(this.StatusConnection);
            this.GroupSysBotStatus.Controls.Add(this.StatusConnectionLabel);
            this.GroupSysBotStatus.Controls.Add(this.ButtonSysbotRead);
            this.GroupSysBotStatus.Location = new System.Drawing.Point(12, 436);
            this.GroupSysBotStatus.Name = "GroupSysBotStatus";
            this.GroupSysBotStatus.Size = new System.Drawing.Size(352, 119);
            this.GroupSysBotStatus.TabIndex = 4;
            this.GroupSysBotStatus.TabStop = false;
            this.GroupSysBotStatus.Text = "Status";
            // 
            // StatusConnection
            // 
            this.StatusConnection.AccessibleName = "StatusConnection";
            this.StatusConnection.AutoSize = true;
            this.StatusConnection.ForeColor = System.Drawing.Color.Red;
            this.StatusConnection.Location = new System.Drawing.Point(67, 16);
            this.StatusConnection.Name = "StatusConnection";
            this.StatusConnection.Size = new System.Drawing.Size(73, 13);
            this.StatusConnection.TabIndex = 15;
            this.StatusConnection.Text = "Disconnected";
            // 
            // StatusConnectionLabel
            // 
            this.StatusConnectionLabel.AccessibleName = "StatusConnectionLabel";
            this.StatusConnectionLabel.AutoSize = true;
            this.StatusConnectionLabel.Location = new System.Drawing.Point(6, 16);
            this.StatusConnectionLabel.Name = "StatusConnectionLabel";
            this.StatusConnectionLabel.Size = new System.Drawing.Size(64, 13);
            this.StatusConnectionLabel.TabIndex = 10;
            this.StatusConnectionLabel.Text = "Connection:";
            // 
            // ButtonSysbotRead
            // 
            this.ButtonSysbotRead.AccessibleName = "ButtonSysbotRead";
            this.ButtonSysbotRead.Enabled = false;
            this.ButtonSysbotRead.Location = new System.Drawing.Point(271, 90);
            this.ButtonSysbotRead.Name = "ButtonSysbotRead";
            this.ButtonSysbotRead.Size = new System.Drawing.Size(75, 23);
            this.ButtonSysbotRead.TabIndex = 14;
            this.ButtonSysbotRead.Text = "Refresh All";
            this.ButtonSysbotRead.UseVisualStyleBackColor = true;
            this.ButtonSysbotRead.Click += new System.EventHandler(this.ButtonSysbotRead_Click);
            // 
            // SysBotTabControl
            // 
            this.SysBotTabControl.AccessibleName = "SysBotTabControl";
            this.SysBotTabControl.Controls.Add(this.TabSysBot);
            this.SysBotTabControl.Controls.Add(this.TabSysBotLog);
            this.SysBotTabControl.Location = new System.Drawing.Point(2, 3);
            this.SysBotTabControl.Name = "SysBotTabControl";
            this.SysBotTabControl.SelectedIndex = 0;
            this.SysBotTabControl.Size = new System.Drawing.Size(540, 431);
            this.SysBotTabControl.TabIndex = 0;
            // 
            // TabSysBot
            // 
            this.TabSysBot.AccessibleName = "TabSysBot";
            this.TabSysBot.Location = new System.Drawing.Point(4, 22);
            this.TabSysBot.Name = "TabSysBot";
            this.TabSysBot.Padding = new System.Windows.Forms.Padding(3);
            this.TabSysBot.Size = new System.Drawing.Size(532, 405);
            this.TabSysBot.TabIndex = 2;
            this.TabSysBot.Text = "Bot";
            this.TabSysBot.UseVisualStyleBackColor = true;
            // 
            // TabSysBotLog
            // 
            this.TabSysBotLog.AccessibleName = "TabSysBotLog";
            this.TabSysBotLog.Controls.Add(this.SysBotLog);
            this.TabSysBotLog.Location = new System.Drawing.Point(4, 22);
            this.TabSysBotLog.Name = "TabSysBotLog";
            this.TabSysBotLog.Padding = new System.Windows.Forms.Padding(3);
            this.TabSysBotLog.Size = new System.Drawing.Size(532, 405);
            this.TabSysBotLog.TabIndex = 3;
            this.TabSysBotLog.Text = "Log";
            this.TabSysBotLog.UseVisualStyleBackColor = true;
            // 
            // SysBotLog
            // 
            this.SysBotLog.AccessibleName = "SysBotLog";
            this.SysBotLog.ImeMode = System.Windows.Forms.ImeMode.NoControl;
            this.SysBotLog.Location = new System.Drawing.Point(6, 6);
            this.SysBotLog.Name = "SysBotLog";
            this.SysBotLog.Size = new System.Drawing.Size(521, 399);
            this.SysBotLog.TabIndex = 5;
            this.SysBotLog.Text = "Started application.";
            // 
            // CartUI
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(540, 562);
            this.Controls.Add(this.SysBotTabControl);
            this.Controls.Add(this.GroupSysBotStatus);
            this.Controls.Add(this.GroupSysBotConnection);
            this.Icon = global::UxieBot.WinForms.Properties.Resources.icon;
            this.Name = "CartUI";
            this.Text = "UxieBot";
            this.Load += new System.EventHandler(this.SysBotUI_Load);
            this.GroupSysBotConnection.ResumeLayout(false);
            this.GroupSysBotConnection.PerformLayout();
            this.GroupSysBotStatus.ResumeLayout(false);
            this.GroupSysBotStatus.PerformLayout();
            this.SysBotTabControl.ResumeLayout(false);
            this.TabSysBotLog.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TextBox TextBoxIP;
        private System.Windows.Forms.Button ButtonConnect;
        private System.Windows.Forms.GroupBox GroupSysBotConnection;
        private System.Windows.Forms.Label LabelPort;
        private System.Windows.Forms.Label LabelIP;
        private System.Windows.Forms.TextBox TextBoxPort;
        private System.Windows.Forms.GroupBox GroupSysBotStatus;
        private System.Windows.Forms.TabControl SysBotTabControl;
        private System.Windows.Forms.TabPage TabSysBot;
        private System.Windows.Forms.Button ButtonSysbotRead;
        private System.Windows.Forms.TabPage TabSysBotLog;
        private System.Windows.Forms.RichTextBox SysBotLog;
        private System.Windows.Forms.Label StatusConnection;
        private System.Windows.Forms.Label StatusConnectionLabel;
    }
}