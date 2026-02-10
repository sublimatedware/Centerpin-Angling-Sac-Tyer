namespace Stage_4_Sac_Tyer
{
    partial class Form1
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Form1));
            this.CmbxSerialList = new System.Windows.Forms.ComboBox();
            this.BtnRefresh = new System.Windows.Forms.Button();
            this.groupBox1 = new System.Windows.Forms.GroupBox();
            this.BtnConnect = new System.Windows.Forms.Button();
            this.groupBox2 = new System.Windows.Forms.GroupBox();
            this.BtnUnTwist = new System.Windows.Forms.Button();
            this.BtnTwist = new System.Windows.Forms.Button();
            this.BtnExpand = new System.Windows.Forms.Button();
            this.BtnCompress = new System.Windows.Forms.Button();
            this.backgroundWorker1 = new System.ComponentModel.BackgroundWorker();
            this.label1 = new System.Windows.Forms.Label();
            this.groupBox1.SuspendLayout();
            this.groupBox2.SuspendLayout();
            this.SuspendLayout();
            // 
            // CmbxSerialList
            // 
            this.CmbxSerialList.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.CmbxSerialList.FormattingEnabled = true;
            this.CmbxSerialList.Location = new System.Drawing.Point(6, 19);
            this.CmbxSerialList.Name = "CmbxSerialList";
            this.CmbxSerialList.Size = new System.Drawing.Size(155, 21);
            this.CmbxSerialList.TabIndex = 0;
            this.CmbxSerialList.SelectedIndexChanged += new System.EventHandler(this.CmbxSerialList_SelectedIndexChanged);
            // 
            // BtnRefresh
            // 
            this.BtnRefresh.Image = ((System.Drawing.Image)(resources.GetObject("BtnRefresh.Image")));
            this.BtnRefresh.Location = new System.Drawing.Point(247, 18);
            this.BtnRefresh.Name = "BtnRefresh";
            this.BtnRefresh.Size = new System.Drawing.Size(23, 23);
            this.BtnRefresh.TabIndex = 1;
            this.BtnRefresh.UseVisualStyleBackColor = true;
            this.BtnRefresh.Click += new System.EventHandler(this.BtnRefresh_Click);
            // 
            // groupBox1
            // 
            this.groupBox1.Controls.Add(this.BtnConnect);
            this.groupBox1.Controls.Add(this.CmbxSerialList);
            this.groupBox1.Controls.Add(this.BtnRefresh);
            this.groupBox1.Location = new System.Drawing.Point(12, 12);
            this.groupBox1.Name = "groupBox1";
            this.groupBox1.Size = new System.Drawing.Size(275, 48);
            this.groupBox1.TabIndex = 2;
            this.groupBox1.TabStop = false;
            this.groupBox1.Text = "Connect Serial Device";
            // 
            // BtnConnect
            // 
            this.BtnConnect.Location = new System.Drawing.Point(167, 18);
            this.BtnConnect.Name = "BtnConnect";
            this.BtnConnect.Size = new System.Drawing.Size(75, 23);
            this.BtnConnect.TabIndex = 2;
            this.BtnConnect.Text = "Connect";
            this.BtnConnect.UseVisualStyleBackColor = true;
            this.BtnConnect.Click += new System.EventHandler(this.BtnConnect_Click);
            // 
            // groupBox2
            // 
            this.groupBox2.Controls.Add(this.BtnUnTwist);
            this.groupBox2.Controls.Add(this.BtnTwist);
            this.groupBox2.Controls.Add(this.BtnExpand);
            this.groupBox2.Controls.Add(this.BtnCompress);
            this.groupBox2.Enabled = false;
            this.groupBox2.Location = new System.Drawing.Point(12, 66);
            this.groupBox2.Name = "groupBox2";
            this.groupBox2.Size = new System.Drawing.Size(87, 137);
            this.groupBox2.TabIndex = 3;
            this.groupBox2.TabStop = false;
            this.groupBox2.Text = "Sack Controls";
            // 
            // BtnUnTwist
            // 
            this.BtnUnTwist.Location = new System.Drawing.Point(6, 106);
            this.BtnUnTwist.Name = "BtnUnTwist";
            this.BtnUnTwist.Size = new System.Drawing.Size(75, 23);
            this.BtnUnTwist.TabIndex = 3;
            this.BtnUnTwist.Text = "UnTwist";
            this.BtnUnTwist.UseVisualStyleBackColor = true;
            // 
            // BtnTwist
            // 
            this.BtnTwist.Location = new System.Drawing.Point(6, 77);
            this.BtnTwist.Name = "BtnTwist";
            this.BtnTwist.Size = new System.Drawing.Size(75, 23);
            this.BtnTwist.TabIndex = 2;
            this.BtnTwist.Text = "Twist";
            this.BtnTwist.UseVisualStyleBackColor = true;
            // 
            // BtnExpand
            // 
            this.BtnExpand.Location = new System.Drawing.Point(6, 48);
            this.BtnExpand.Name = "BtnExpand";
            this.BtnExpand.Size = new System.Drawing.Size(75, 23);
            this.BtnExpand.TabIndex = 1;
            this.BtnExpand.Text = "Expand";
            this.BtnExpand.UseVisualStyleBackColor = true;
            this.BtnExpand.Click += new System.EventHandler(this.BtnExpand_Click);
            // 
            // BtnCompress
            // 
            this.BtnCompress.Location = new System.Drawing.Point(6, 19);
            this.BtnCompress.Name = "BtnCompress";
            this.BtnCompress.Size = new System.Drawing.Size(75, 23);
            this.BtnCompress.TabIndex = 0;
            this.BtnCompress.Text = "Compress";
            this.BtnCompress.UseVisualStyleBackColor = true;
            this.BtnCompress.Click += new System.EventHandler(this.BtnCompress_Click);
            // 
            // label1
            // 
            this.label1.BackColor = System.Drawing.Color.DarkRed;
            this.label1.BorderStyle = System.Windows.Forms.BorderStyle.Fixed3D;
            this.label1.Location = new System.Drawing.Point(179, 118);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(30, 30);
            this.label1.TabIndex = 4;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.SystemColors.Control;
            this.ClientSize = new System.Drawing.Size(302, 224);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.groupBox2);
            this.Controls.Add(this.groupBox1);
            this.Name = "Form1";
            this.Text = "Tight-Sac O-Matic 69000 Controller";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.groupBox1.ResumeLayout(false);
            this.groupBox2.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.ComboBox CmbxSerialList;
        private System.Windows.Forms.Button BtnRefresh;
        private System.Windows.Forms.GroupBox groupBox1;
        private System.Windows.Forms.Button BtnConnect;
        private System.Windows.Forms.GroupBox groupBox2;
        private System.Windows.Forms.Button BtnUnTwist;
        private System.Windows.Forms.Button BtnTwist;
        private System.Windows.Forms.Button BtnExpand;
        private System.Windows.Forms.Button BtnCompress;
        private System.ComponentModel.BackgroundWorker backgroundWorker1;
        private System.Windows.Forms.Label label1;
    }
}

