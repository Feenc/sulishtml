using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace wpf0223
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void Button_Click(object sender, RoutedEventArgs e)
        {
            string nev = TextBox1.Text;
            string szhely = TextBox2.Text;
            string kor = TextBox3.Text;
            if(nev==""|| szhely == "" || kor == "")
            {
                MessageBox.Show("Töltsd ki mindet!");
            }
            else
            {
                listBox.Items.Add(nev + ", " + szhely + ", " + kor);

                TextBox1.Text = "";
                TextBox2.Text = "";
                TextBox3.Text = "";
            }
            
        }

        private void TextBox_TextChanged(object sender, TextChangedEventArgs e)
        {

        }
    }
}
