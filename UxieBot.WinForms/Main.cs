using System;
using System.Threading;
using System.Windows.Forms;

namespace UxieBot.WinForms
{
    public partial class Main : Form
    {

        public Main()
        {
            InitializeComponent();
        }

        private void BtnCartridge_Click(object sender, EventArgs e)
        {
            var t = new Thread(() => Application.Run(new CartUI()));
            t.Start();
            Close();
        }

        private void BtnShowdown_Click(object sender, EventArgs e)
        {
            MessageBox.Show("Showdown coming soonTM",
                "UxieBot",
                MessageBoxButtons.OK
            );
        }
    }
}
