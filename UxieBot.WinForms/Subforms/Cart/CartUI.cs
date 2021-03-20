using SysBot.Base;
using System;
using System.Drawing;
using System.Windows.Forms;
using UxieBot.Cart;

namespace UxieBot.WinForms
{
    public partial class CartUI : Form
    {
#pragma warning disable CA1416 // Do not catch Win7 warning

        private static readonly string WorkingDirectory = Application.StartupPath;
        //private static readonly string ConfigPath = Path.CombineArrays(WorkingDirectory, "config.json");


        public CartUI()
        {
            InitializeComponent();
        }

        public Injector SwitchInjector = new Injector();
        readonly SwitchConnectionConfig cfg = new SwitchConnectionConfig();
        readonly PointerHandler PointerHandler = new PointerHandler();
        public bool Connected = false;
        public ISwitchConnectionSync sb;

        // Declare offsets


        public void SysBotUI_Load(object sender, EventArgs e)
        {

        }

        // sb and getting values
        private void ButtonConnect_Click(object sender, EventArgs e)
        {
            int Port = int.Parse(TextBoxPort.Text);
            if (Connected == false)
            {
                // Connect button behaviour
                cfg.IP = TextBoxIP.Text;
                cfg.Port = Port;
                sb = cfg.CreateSync();
                sb.Connect();

                ReloadValues();
                // Toggle buttons and fields
                TextBoxIP.Enabled = false;
                TextBoxPort.Enabled = false;
                ButtonSysbotRead.Enabled = true;

                StatusConnection.ForeColor = Color.Green;
                StatusConnection.Text = "Connected";
                Connected = true;
                ButtonConnect.Text = "Disconnect";
                SysBotLog.Text += Environment.NewLine + "Successfully connected.";
            }
            else
            {
                // Disconnect button behaviour
                sb.Disconnect();
                // Toggle buttons and fields
                TextBoxIP.Enabled = true;
                TextBoxPort.Enabled = true;
                ButtonSysbotRead.Enabled = false;

                StatusConnection.ForeColor = Color.Red;
                StatusConnection.Text = "Disconnected";
                Connected = false;
                ButtonConnect.Text = "Connect";
                SysBotLog.Text += Environment.NewLine + "Successfully disconnected.";
            }
        }
        private void ButtonSysbotRead_Click(object sender, EventArgs e)
        {
            ReloadValues();
        }

        private void ReloadValues()
        {
            //// Get offsets from pointers


            //// Read values from offsets


            SysBotLog.Text += Environment.NewLine + "Successfully loaded values.";
        }
    }
}