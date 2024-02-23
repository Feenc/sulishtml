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

namespace lasdmk
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        bool betoltott=false;
        public MainWindow()
        {
            InitializeComponent();
            this.betoltott = true;
        }
        double[] ertekek = new double[4] { 1, 1, 1, 1 };
        private void Slider_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            if (betoltott)
            {
                ertekek[0] = slider1.Value;
                stop1.Opacity = (1 - ertekek[0]) * ertekek[1];
                stop2.Opacity = ertekek[0] * ertekek[3];
            }
            
        }

        private void slider2_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            if (betoltott)
            {
                ertekek[1] = slider2.Value;
                stop2.Opacity = (1 - ertekek[0]) * ertekek[1];
                stop3.Opacity = (1 - ertekek[1]) * ertekek[2];
            }
            
        }
        private void slider3_ValueChanged(object sender, RoutedPropertyChangedEventArgs<double> e)
        {
            if (betoltott)
            {
                ertekek[1] = slider2.Value;
                stop3.Opacity = (1 - ertekek[0]) * ertekek[1];
                stop4.Opacity = (1 - ertekek[1]) * ertekek[2];
            }
            
        }


    }
}
