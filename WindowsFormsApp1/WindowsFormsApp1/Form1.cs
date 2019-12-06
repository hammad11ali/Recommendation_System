using System;
using System.Linq;
using System.Windows.Forms;
using System.IO;

namespace WindowsFormsApp1
{
    public partial class Form1 : Form
    {
        StreamWriter results = new StreamWriter(Directory.GetCurrentDirectory() + "MetaData.txt", true);
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            string path = "";
            OpenFileDialog fileDialog = new OpenFileDialog();
            fileDialog.Title = "Choose image file";
            fileDialog.Filter = "CSV File|*.csv";
            if (fileDialog.ShowDialog() == DialogResult.OK)
            {
                path = fileDialog.FileName;
            }
            else
            {
                MessageBox.Show("Invalid File");
                return;
            }
            StreamReader reader = new StreamReader(path);
            reader.ReadLine();
            int i = 0;
            while (!reader.EndOfStream)
            {
                var line = reader.ReadLine();
                var values = line.Split(',');
                results.Write(i + "," + values[1]);
                checktags(values[2]);
                results.WriteLine();
                i++;
            }
            MessageBox.Show("Done. File in bin folder");
        }
        void checktags(string value)
        {
            var tags = value.Split('|');
            if (tags.Contains<string>("Action")) results.Write(","+"1");
            else results.Write("," + "0");
            if (tags.Contains<string>("Adventure")) results.Write("," + "1");
            else results.Write("," + "0");
            if (tags.Contains<string>("Animation")) results.Write("," + "1");
            else results.Write("," + "0");
            if (tags.Contains<string>("Children's")) results.Write("," + "1");
            else results.Write("," + "0");
            if (tags.Contains<string>("Comedy")) results.Write("," + "1");
            else results.Write("," + "0");
            if (tags.Contains<string>("Crime")) results.Write("," + "1");
            else results.Write("," + "0");
            if (tags.Contains<string>("Documentary")) results.Write("," + "1");
            else results.Write("," + "0");
            if (tags.Contains<string>("Drama")) results.Write("," + "1");
            else results.Write("," + "0");
            if (tags.Contains<string>("Fantasy")) results.Write("," + "1");
            else results.Write("," + "0");
            if (tags.Contains<string>("Film-Noir")) results.Write("," + "1");
            else results.Write("," + "0");
            if (tags.Contains<string>("Horror")) results.Write("," + "1");
            else results.Write("," + "0");
            if (tags.Contains<string>("Musical")) results.Write("," + "1");
            else results.Write("," + "0");
            if (tags.Contains<string>("Mystery")) results.Write("," + "1");
            else results.Write("," + "0");
            if (tags.Contains<string>("Romance")) results.Write("," + "1");
            else results.Write("," + "0");
            if (tags.Contains<string>("Sci-Fi")) results.Write("," + "1");
            else results.Write("," + "0");
            if (tags.Contains<string>("Thriller")) results.Write("," + "1");
            else results.Write("," + "0");
            if (tags.Contains<string>("War")) results.Write("," + "1");
            else results.Write("," + "0");
            if (tags.Contains<string>("Western")) results.Write("," + "1");
            else results.Write("," + "0");
        }
    }
}
