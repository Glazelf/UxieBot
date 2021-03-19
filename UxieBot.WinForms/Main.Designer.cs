
namespace UxieBot.WinForms
{
    partial class Main
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
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

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnCartridge = new System.Windows.Forms.Button();
            this.btnShowdown = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // btnCartridge
            // 
            this.btnCartridge.AccessibleName = "buttonCartridge";
            this.btnCartridge.Location = new System.Drawing.Point(64, 17);
            this.btnCartridge.Name = "btnCartridge";
            this.btnCartridge.Size = new System.Drawing.Size(150, 52);
            this.btnCartridge.TabIndex = 0;
            this.btnCartridge.Text = "Cart Bot";
            this.btnCartridge.UseVisualStyleBackColor = true;
            this.btnCartridge.Click += new System.EventHandler(this.BtnCartridge_Click);
            // 
            // btnShowdown
            // 
            this.btnShowdown.AccessibleName = "buttonShowdown";
            this.btnShowdown.Location = new System.Drawing.Point(64, 87);
            this.btnShowdown.Name = "btnShowdown";
            this.btnShowdown.Size = new System.Drawing.Size(150, 52);
            this.btnShowdown.TabIndex = 1;
            this.btnShowdown.Text = "Showdown";
            this.btnShowdown.UseVisualStyleBackColor = true;
            this.btnShowdown.Click += new System.EventHandler(this.BtnShowdown_Click);
            // 
            // Main
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(292, 170);
            this.Controls.Add(this.btnShowdown);
            this.Controls.Add(this.btnCartridge);
            this.Icon = global::UxieBot.WinForms.Properties.Resources.icon;
            this.Name = "Main";
            this.Text = "UxieBot";
            this.ResumeLayout(false);

        }

        private System.Windows.Forms.Button btnCartridge;
        private System.Windows.Forms.Button btnShowdown;

    }
}

