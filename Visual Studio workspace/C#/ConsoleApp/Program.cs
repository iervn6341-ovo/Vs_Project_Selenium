using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp
{
        class Program
        {
                static void Main(string [ ] args)
                {
                        Chef thechef = new Chef();
                        thechef.canchop();
                        thechef.cancook();

                        taiwanesechef taichef = new taiwanesechef();
                        taichef.cancook();

                        thechef.cancook();

                        Console.ReadLine();
                }
        }
        class Chef
        {
                public void canchop()
                {
                        Console.WriteLine("I can chop vegetables");
                }
                public virtual void cancook()
                {
                        Console.WriteLine("I can cook some of steaks");
                }
        }
        class taiwanesechef : Chef
        {
                public override void cancook()
                {
                        Console.WriteLine("I can fried chicken");
                }
        }

}
