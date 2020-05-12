import wnutils.xml as wx
import matplotlib.pyplot as plt

my_xml1 = wx.Xml('no-sdot-no-thermo.xml')
my_xml2 = wx.Xml('with-thermo-no-sdot.xml')
#my_xml3 = wx.Xml('out10-cst-with-sdot.xml')


y1 = my_xml1.get_abundances_vs_nucleon_number(nucleon = 'a', zone_xpath="[last()]")
y2 = my_xml2.get_abundances_vs_nucleon_number(nucleon = 'a', zone_xpath="[last()]")
#y3 = my_xml3.get_abundances_vs_nucleon_number(nucleon = 'a', zone_xpath="[last()]")

line1, = plt.plot(y1[0,:])
line2, = plt.plot(y2[0,:])
#line3, = plt.plot(y3[0,:])

plt.xlabel('Mass Number, A')
plt.ylabel('Abundance per nucleon, Y(A)')
plt.xlim(0,280)
plt.ylim(1.e-10,1.e-1)
plt.yscale('log')
#plt.legend((line1,line2),(r'$\dot s = 0$',r'$\dot s \neq 0 $'))
plt.legend((line1,line2),('no thermo','with thermo'))
plt.show()
