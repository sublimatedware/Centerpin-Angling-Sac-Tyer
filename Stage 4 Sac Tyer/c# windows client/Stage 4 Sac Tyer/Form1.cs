using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO.Ports;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using System.Threading.Tasks;
using System.Management;
using System.Windows.Forms;
using System.Threading;
using System.CodeDom;


namespace Stage_4_Sac_Tyer
{
    public partial class Form1 : Form
    {
        SerialPort serialPort;
        public static char[] rxBuffer = new char[128];

        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            LoadSerialPorts();
        }

        private void CmbxSerialList_SelectedIndexChanged(object sender, EventArgs e)
        {

        }

        private void LoadSerialPorts()
        {
            string[] ports = SerialPort.GetPortNames();
            CmbxSerialList.Items.Clear();
            CmbxSerialList.Items.AddRange(ports);
        }

        private void BtnRefresh_Click(object sender, EventArgs e)
        {
            LoadSerialPorts();
        }

        private void BtnConnect_Click(object sender, EventArgs e)
        {
            if (CmbxSerialList.SelectedItem != null)
            {
                string selectedPort = CmbxSerialList.SelectedItem.ToString();
                try
                {
                    serialPort = new SerialPort(selectedPort, 115200);
                    serialPort.Open();
                    serialPort.Write(new char[] {'a','y','y'}, 0, 3);
                    Thread.Sleep(10);
                    char[] buffer = new char[4];
                    serialPort.Read(buffer, 0, 4);
                    Console.Write(buffer);
                    if (buffer.SequenceEqual(new char[] { 'l', 'm', 'a', 'o' }) == false)
                    {
                        serialPort.Close();
                        throw new ArgumentException("The device did not respond to the request to connect. Maybe the device is not the Tight-Sac O-Matic 69000?");
                    }
                    else
                    {
                        MessageBox.Show("Successfully connected to the Tight-Sac O-Matic 69000!");
                        serialPort.DataReceived += new SerialDataReceivedEventHandler(DataReceivedHandler);
                        serialPort.Write(new char[] { 'o', 'k', 'k' }, 0, 3);
                        BtnConnect.Enabled = false;
                        BtnRefresh.Enabled = false;
                        CmbxSerialList.Enabled = false;
                        groupBox2.Enabled = true;
                    }
                        
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error connecting to device: " + ex.Message);
                    return;
                }
            }
            else
            {
                MessageBox.Show("Please select a serial device from the list.");
            }
        }

        private void BtnCompress_Click(object sender, EventArgs e)
        {
            serialPort.Write(new char[] { 'a', 'b', 'a' }, 0, 3);
        }

        private void BtnExpand_Click(object sender, EventArgs e)
        {
            serialPort.Write(new char[] { 'b', 'a', 'b' }, 0, 3);
        }

        private static void DataReceivedHandler(object sender, SerialDataReceivedEventArgs e)
        {
            SerialPort sp = (SerialPort)sender;
            Array.Clear(rxBuffer, 0, 128);
            sp.Read(rxBuffer, 0, 3);
            Console.Write(rxBuffer);
        }
    }
}