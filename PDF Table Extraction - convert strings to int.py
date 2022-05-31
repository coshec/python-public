Microsoft Windows [Version 10.0.18362.720]
(c) 2019 Microsoft Corporation. All rights reserved.

C:\Users\kaushik.kochhar>path
PATH=C:\Program Files (x86)\Common Files\Oracle\Java\javapath;C:\Program Files (x86)\Seclore\FileSecure\Desktop Client;C:\Program Files (x86)\Seclore\FileSecure\Desktop Client\Upgrade Manager;C:\Program Files (x86)\Seclore\FileSecure\Desktop Client;C:\Program Files (x86)\Seclore\FileSecure\Desktop Client\x64;C:\Program Files (x86)\Intel\iCLS Client\;C:\Program Files\Intel\iCLS Client\;C:\WINDOWS\system32;C:\WINDOWS;C:\WINDOWS\System32\Wbem;C:\WINDOWS\System32\WindowsPowerShell\v1.0\;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files\Intel\Intel(R) Management Engine Components\DAL;C:\Program Files (x86)\Intel\Intel(R) Management Engine Components\IPT;C:\Program Files\Intel\Intel(R) Management Engine Components\IPT;C:\WINDOWS\System32\OpenSSH\;C:\Program Files\Intel\WiFi\bin\;C:\Program Files\Common Files\Intel\WirelessCommon\;C:\Program Files\nodejs\;C:\ProgramData\chocolatey\bin;C:\Users\kaushik.kochhar\Anaconda3;C:\Users\kaushik.kochhar\Anaconda3\scripts;C:\Users\kaushik.kochhar\AppData\Local\Microsoft\WindowsApps;;C:\Users\kaushik.kochhar\AppData\Local\Programs\Microsoft VS Code\bin

C:\Users\kaushik.kochhar>cd anaconda3

C:\Users\kaushik.kochhar\Anaconda3>python
Python 3.7.3 (default, Mar 27 2019, 17:13:21) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32

Warning:
This Python interpreter is in a conda environment, but the environment has
not been activated.  Libraries may fail to load.  To activate this environment
please see https://conda.io/activation

Type "help", "copyright", "credits" or "license" for more information.
>>> from tabula import read_pdf
>>> import pandas as pd
>>> df=read_pdf(r"C:\Users\kaushik.kochhar\Downloads\PN14092018.pdf",pages="all")
>>> df
[    GA Id                                            GA Name  ...        Unnamed: 0             Unnamed: 1
0     NaN                                                NaN  ...  PNG\rConnections  Steel Pipe\r(Inch-km)
1    GA_2           Cachar, Hailakandi & Karimganj Districts  ...             95001                    751
2    GA_3             Kamrup & Kamrup Metropolitan Districts  ...            321001                    961
3    GA_4              Aurangabad, Kaimur & Rohtas Districts  ...             14271                    800
4    GA_5                                 Begusarai District  ...            169787                    762
5    GA_6                           Gaya & Nalanda Districts  ...             37591                   1304
6    GA_7                        Diu & Gir Somnath Districts  ...             91000                    188
7    GA_8  Surendranagar District (Except areas already\r...  ...             87005                    839
8    GA_9                           Barwala & Ranpur Talukas  ...             12098                    209
9   GA_10  Navsari Dist (Except areas already\rauthorized...  ...             90191                   1010
10  GA_11                                  Junagadh District  ...             77400                   3186
11  GA_12  Kheda Districts (Except areas already\rauthori...  ...            175007                   1010
12  GA_13                        Narmada (Rajpipla) District  ...              1750                     55
13  GA_14                                 Porbandar District  ...             60464                    704
14  GA_15  Panchkula District  (Except areas already\raut...  ...             32360                      -
15  GA_16   Bhiwani, Charkhi Dadri & Mahendragarh\rDistricts  ...            150464                   1010
16  GA_17                                     Hisar District  ...            251370                   1991
17  GA_19  Sonipat District (Except areas already\rauthor...  ...             98000                   1183
18  GA_20                             Nuh & Palwal Districts  ...            181019                    803
19  GA_21                 Bilaspur, Hamirpur & Una Districts  ...             28170                      -
20  GA_22             Bokaro, Hazaribagh & Ramgarh Districts  ...             79052                   1300
21  GA_23                        Giridih & Dhanbad Districts  ...             50000                    650
22  GA_24                  Chitradurga & Devangere Districts  ...            101000                     75

[23 rows x 9 columns],     GA Id                                            GA Name  ...        Unnamed: 0             Unnamed: 1
0     NaN                                                NaN  ...  PNG\rConnections  Steel Pipe\r(Inch-km)
1   GA_25                                     Udupi District  ...            110099                    569
2   GA_26                         Balliari & Gadag Districts  ...             53850                   1365
3   GA_27                                     Bidar District  ...              6200                    143
4   GA_28                         Dakshina Kannada Districts  ...            350000                   1250
5   GA_29                                Ramanagara District  ...            113115                    354
6   GA_30                      Kozhikode & wayanad Districts  ...            421277                    927
7   GA_31                               Malappuram Districts  ...            338518                   1671
8   GA_32                  Kannur, Kasargod & Mahe Districts  ...            367176                   1103
9   GA_33                      Palakkad & Thrissur Districts  ...            600000                   2126
10  GA_34                         Bhopal & Rajgarh Districts  ...            550222                   2508
11  GA_35                                      Guna District  ...              4900                    400
12  GA_36                                      Rewa District  ...              7861                    950
13  GA_37                          Satna & Shandol Districts  ...             15600                    196
14  GA_38                  Ahmednagar & Aurangabad Districts  ...            708100                   2109
15  GA_39  Valsad (except area already authorized), Dhule...  ...            937965                   2181
16  GA_40                       Latur & Osamanabad Districts  ...              9999                     10
17  GA_41                          Sangli & Satara Districts  ...            376700                   2112
18  GA_42                                Sindhudurg District  ...             25779                    759
19  GA_43                         Angul & Dhekanal Districts  ...             22600                   1464
20  GA_44                  Sundargarh & Jharsuguda Districts  ...            100000                    500
21  GA_45           Balasore, Bhadrak & Mayurbhanj Districts  ...            150464                    506
22  GA_46            Bargarh, Debagarh & Sambalpur Districts  ...             13910                    650
23  GA_47                  Ganjam, Nayagarh & Puri Districts  ...             51000                    650
24  GA_48               Jagatsinghpur & Kendrapara Districts  ...             12550                    791

[25 rows x 9 columns],     GA Id                                            GA Name  ...        Unnamed: 0             Unnamed: 1
0     NaN                                                NaN  ...  PNG\rConnections  Steel Pipe\r(Inch-km)
1   GA_49                       Jajpur & Kendujhar Districts  ...             18200                   2442
2   GA_50                  Karaikal & Nagapattinam Districts  ...            166644                    495
3   GA_51                                Puducherry District  ...            275000                   2100
4   GA_52  SAS Nagar district (Except areas already\rauth...  ...            520200                   2610
5   GA_55              Barmer, Jaisalmer & Jodhpur Districts  ...            551111                      -
6   GA_56      Alwar (Other than Bhiwadi) & Jaipur Districts  ...           1320000                  12030
7   GA_57  Kota (except area already authorized), Baran\r...  ...             60300                   3393
8   GA_58                          Bilwara & Bundi Districts  ...            270056                    659
9   GA_59  Chittorgarh (Other than Rawatbhata) &\rUdaipur...  ...            400583                   1568
10  GA_60                                   Dholpur District  ...             18000                    412
11  GA_61                               Kanchipuram District  ...           1151111                    668
12  GA_62                     Chennai & Tiruvallur Districts  ...           3300000                   6666
13  GA_63                                Coimbatore District  ...            912783                   2500
14  GA_64       Cuddalore, Nagapatinam & Tiruvarur Districts  ...            300089                    839
15  GA_65                            Ramanathapuram District  ...             41311                    251
16  GA_66                                     Salem District  ...            337062                   1368
17  GA_67                                  Tiruppur District  ...            375005                    829
18  GA_68           Bhadradri Kothagudem & Khammam Districts  ...             99999                    800
19  GA_69  Jagtial, Peddapalle, Karimnagar & Rajanna\rSir...  ...              5731                    520
20  GA_70  Jangaon, Jayashankar Boopalpally,\rMahbubabad,...  ...             99999                    800
21  GA_71             Medak, Siddipet & Sangareddy Districts  ...            310770                   5076

[22 rows x 9 columns],     GA Id                                            GA Name  ...        Unnamed: 0             Unnamed: 1
0     NaN                                                NaN  ...  PNG\rConnections  Steel Pipe\r(Inch-km)
1   GA_72           Medchal Rangareddy & Vikarabad Districts  ...            415000                   2020
2   GA_73  Nalgonda. Suryapet & Yadadri Bhuvanagiri\rDist...  ...            350000                   1500
3   GA_74                                    Gomati District  ...             11514                    170
4   GA_75  West Tripura (Except areas already\rauthorized...  ...             15800                     60
5   GA_76  Bulandshahr (Except areas already\rauthorized)...  ...            143404                   1662
6   GA_77  Allahabad (Except areas already authorized),\r...  ...             58658                    680
7   GA_78          Amethi, Pratapgarh & Rai Bareli Districts  ...             18169                    385
8   GA_79           Auraiya, Kanpur Dehat & Etawah Districts  ...            118800                   1602
9   GA_80                     Faizabad & Sultanpur Districts  ...              4000                    350
10  GA_81           Gorakhpur, Sant Kabir Nagar & Kushinagar  ...            178200                   5814
11  GA_82  Meerut (Except areas already authorized),\rMuz...  ...            105543                   1755
12  GA_83  Moradabad (Except areas already authorized)\rD...  ...            154800                    792
13  GA_84           Unnao ( Except areas already authorized)  ...              3000                    150
14  GA_85                                  Dehradun District  ...            300001                    900
15  GA_86                                   Burdwan District  ...            247852                   2230
16  4,346                                        2,10,48,045  ...               NaN                    NaN

[17 rows x 9 columns]]
>>> len(df)
4
>>> dh=pd.DataFrame(df)
>>> dh
                                                   0
0      GA Id                                     ...
1      GA Id                                     ...
2      GA Id                                     ...
3      GA Id                                     ...
>>> df[0]
    GA Id                                            GA Name  ...        Unnamed: 0             Unnamed: 1
0     NaN                                                NaN  ...  PNG\rConnections  Steel Pipe\r(Inch-km)
1    GA_2           Cachar, Hailakandi & Karimganj Districts  ...             95001                    751
2    GA_3             Kamrup & Kamrup Metropolitan Districts  ...            321001                    961
3    GA_4              Aurangabad, Kaimur & Rohtas Districts  ...             14271                    800
4    GA_5                                 Begusarai District  ...            169787                    762
5    GA_6                           Gaya & Nalanda Districts  ...             37591                   1304
6    GA_7                        Diu & Gir Somnath Districts  ...             91000                    188
7    GA_8  Surendranagar District (Except areas already\r...  ...             87005                    839
8    GA_9                           Barwala & Ranpur Talukas  ...             12098                    209
9   GA_10  Navsari Dist (Except areas already\rauthorized...  ...             90191                   1010
10  GA_11                                  Junagadh District  ...             77400                   3186
11  GA_12  Kheda Districts (Except areas already\rauthori...  ...            175007                   1010
12  GA_13                        Narmada (Rajpipla) District  ...              1750                     55
13  GA_14                                 Porbandar District  ...             60464                    704
14  GA_15  Panchkula District  (Except areas already\raut...  ...             32360                      -
15  GA_16   Bhiwani, Charkhi Dadri & Mahendragarh\rDistricts  ...            150464                   1010
16  GA_17                                     Hisar District  ...            251370                   1991
17  GA_19  Sonipat District (Except areas already\rauthor...  ...             98000                   1183
18  GA_20                             Nuh & Palwal Districts  ...            181019                    803
19  GA_21                 Bilaspur, Hamirpur & Una Districts  ...             28170                      -
20  GA_22             Bokaro, Hazaribagh & Ramgarh Districts  ...             79052                   1300
21  GA_23                        Giridih & Dhanbad Districts  ...             50000                    650
22  GA_24                  Chitradurga & Devangere Districts  ...            101000                     75

[23 rows x 9 columns]
>>> df[1]
    GA Id                                            GA Name  ...        Unnamed: 0             Unnamed: 1
0     NaN                                                NaN  ...  PNG\rConnections  Steel Pipe\r(Inch-km)
1   GA_25                                     Udupi District  ...            110099                    569
2   GA_26                         Balliari & Gadag Districts  ...             53850                   1365
3   GA_27                                     Bidar District  ...              6200                    143
4   GA_28                         Dakshina Kannada Districts  ...            350000                   1250
5   GA_29                                Ramanagara District  ...            113115                    354
6   GA_30                      Kozhikode & wayanad Districts  ...            421277                    927
7   GA_31                               Malappuram Districts  ...            338518                   1671
8   GA_32                  Kannur, Kasargod & Mahe Districts  ...            367176                   1103
9   GA_33                      Palakkad & Thrissur Districts  ...            600000                   2126
10  GA_34                         Bhopal & Rajgarh Districts  ...            550222                   2508
11  GA_35                                      Guna District  ...              4900                    400
12  GA_36                                      Rewa District  ...              7861                    950
13  GA_37                          Satna & Shandol Districts  ...             15600                    196
14  GA_38                  Ahmednagar & Aurangabad Districts  ...            708100                   2109
15  GA_39  Valsad (except area already authorized), Dhule...  ...            937965                   2181
16  GA_40                       Latur & Osamanabad Districts  ...              9999                     10
17  GA_41                          Sangli & Satara Districts  ...            376700                   2112
18  GA_42                                Sindhudurg District  ...             25779                    759
19  GA_43                         Angul & Dhekanal Districts  ...             22600                   1464
20  GA_44                  Sundargarh & Jharsuguda Districts  ...            100000                    500
21  GA_45           Balasore, Bhadrak & Mayurbhanj Districts  ...            150464                    506
22  GA_46            Bargarh, Debagarh & Sambalpur Districts  ...             13910                    650
23  GA_47                  Ganjam, Nayagarh & Puri Districts  ...             51000                    650
24  GA_48               Jagatsinghpur & Kendrapara Districts  ...             12550                    791

[25 rows x 9 columns]
>>> dg=pd.concat(df,index=False)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: concat() got an unexpected keyword argument 'index'
>>> dg=pd.concat(df,ignore_index=False)
>>> dg
    GA Id                                            GA Name  ...        Unnamed: 0             Unnamed: 1
0     NaN                                                NaN  ...  PNG\rConnections  Steel Pipe\r(Inch-km)
1    GA_2           Cachar, Hailakandi & Karimganj Districts  ...             95001                    751
2    GA_3             Kamrup & Kamrup Metropolitan Districts  ...            321001                    961
3    GA_4              Aurangabad, Kaimur & Rohtas Districts  ...             14271                    800
4    GA_5                                 Begusarai District  ...            169787                    762
..    ...                                                ...  ...               ...                    ...
12  GA_83  Moradabad (Except areas already authorized)\rD...  ...            154800                    792
13  GA_84           Unnao ( Except areas already authorized)  ...              3000                    150
14  GA_85                                  Dehradun District  ...            300001                    900
15  GA_86                                   Burdwan District  ...            247852                   2230
16  4,346                                        2,10,48,045  ...               NaN                    NaN

[87 rows x 9 columns]
>>> dg['Winning Entity'].value_counts()
Adani Gas Limited                                                                   13
Bharat Gas Resources Limited                                                        11
Torrent Gas Private Limited                                                         10
IndianOil-Adani Gas Private Limited                                                  9
Indian Oil Corporation Limited                                                       7
GAIL Gas Limited                                                                     5
Megha Engineering & Infrastructures Limited                                          4
Maharashtra Natural Gas Limited                                                      3
Consortium of Think Gas Investments PTE\rLimited                                     2
Tripura Natural Gas Company Limited                                                  2
Green Gas Limited                                                                    2
Consortium of AG&P LNG Marketing Pte Ltd.\r& Atlantic Gulf & Pacific                 2
Consortium of Assam Gas Company Limited,\rOil India Limited and GAIL Gas Limited     2
Unison Enviro Private Limited                                                        2
Consortium of Haryana City Gas Kapil Chopra\rEnterprise & Rati Chopra                1
IRM Energy Private Limited                                                           1
Indraprastha Gas Limited                                                             1
Gujarat Gas Limited                                                                  1
Essel Gas Company Limited                                                            1
Consortium of SKN Haryana City Gas\rDistribution Pvt. Ltd and Chopra Electricals     1
Hindustan Petroleum Corporation Limited                                              1
AG&P LNG Marketing Pte. Ltd.                                                         1
Name: Winning Entity, dtype: int64
>>> dg.groupby('Winning Entity').sum()
                                                    Network\rTariff\r(Rs/MMBTU)  Compression\rCharge\r(Rs/kg)
Winning Entity
AG&P LNG Marketing Pte. Ltd.                                              30.00                          2.00
Adani Gas Limited                                                        390.00                         26.00
Bharat Gas Resources Limited                                             330.00                         22.00
Consortium of AG&P LNG Marketing Pte Ltd.\r& At...                        60.00                          4.00
Consortium of Assam Gas Company Limited,\rOil I...                        60.00                          4.00
Consortium of Haryana City Gas Kapil Chopra\rEn...                        30.00                          2.00
Consortium of SKN Haryana City Gas\rDistributio...                        30.00                          2.00
Consortium of Think Gas Investments PTE\rLimited                          60.00                          4.00
Essel Gas Company Limited                                                 30.06                          2.07
GAIL Gas Limited                                                         150.00                         10.00
Green Gas Limited                                                         60.00                          4.00
Gujarat Gas Limited                                                       30.00                          2.00
Hindustan Petroleum Corporation Limited                                   30.00                          2.00
IRM Energy Private Limited                                                30.00                          2.00
Indian Oil Corporation Limited                                           210.00                         14.00
IndianOil-Adani Gas Private Limited                                      270.00                         18.00
Indraprastha Gas Limited                                                  30.00                          2.00
Maharashtra Natural Gas Limited                                           90.00                          6.00
Megha Engineering & Infrastructures Limited                              120.00                          8.00
Torrent Gas Private Limited                                              300.00                         20.00
Tripura Natural Gas Company Limited                                      121.58                          6.75
Unison Enviro Private Limited                                             60.00                          4.00
>>> map
{'GA Id': 'GA Id', 'GA Name': 'GA Name', 'State': 'State', 'Winning Entity': 'Winning Entity', 'Network\rTariff\r(Rs/MMBTU)': 'Network\rTariff\r(Rs/MMBTU)', 'Compression\rCharge\r(Rs/kg)': 'Compression\rCharge\r(Rs/kg)', 'Work Program': 'CNGStations', 'Unnamed: 0': 'PNGConnections', 'Unnamed: 1': 'SteelPipe'}
>>> dg.rename(columns=map,inplace=True)
>>> dg
    GA Id                                            GA Name  ...    PNGConnections              SteelPipe
0     NaN                                                NaN  ...  PNG\rConnections  Steel Pipe\r(Inch-km)
1    GA_2           Cachar, Hailakandi & Karimganj Districts  ...             95001                    751
2    GA_3             Kamrup & Kamrup Metropolitan Districts  ...            321001                    961
3    GA_4              Aurangabad, Kaimur & Rohtas Districts  ...             14271                    800
4    GA_5                                 Begusarai District  ...            169787                    762
..    ...                                                ...  ...               ...                    ...
12  GA_83  Moradabad (Except areas already authorized)\rD...  ...            154800                    792
13  GA_84           Unnao ( Except areas already authorized)  ...              3000                    150
14  GA_85                                  Dehradun District  ...            300001                    900
15  GA_86                                   Burdwan District  ...            247852                   2230
16  4,346                                        2,10,48,045  ...               NaN                    NaN

[87 rows x 9 columns]
>>> dg.columns
Index(['GA Id', 'GA Name', 'State', 'Winning Entity',
       'Network\rTariff\r(Rs/MMBTU)', 'Compression\rCharge\r(Rs/kg)',
       'CNGStations', 'PNGConnections', 'SteelPipe'],
      dtype='object')
>>> dg.groupby('Winning Entity')['CNGStations', 'PNGConnections', 'SteelPipe'].sum()
__main__:1: FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.
                                                                  CNGStations  ...                                    SteelPipe
Winning Entity                                                                 ...                                      
AG&P LNG Marketing Pte. Ltd.                                              111  ...                                          668
Adani Gas Limited                                   2042530126060112025704075  ...  8392091010101070410108035695066591568839829
Bharat Gas Resources Limited                            102448106642111101920  ...         -13651431962109211214646507912442385
Consortium of AG&P LNG Marketing Pte Ltd.\r& At...                       8011  ...                                         -251
Consortium of Assam Gas Company Limited,\rOil I...                       2151  ...                                       751961
Consortium of Haryana City Gas Kapil Chopra\rEn...                         46  ...                                         1991
Consortium of SKN Haryana City Gas\rDistributio...                        130  ...                                         2100
Consortium of Think Gas Investments PTE\rLimited                        25104  ...                                      7622508
Essel Gas Company Limited                                                  14  ...                                          412
GAIL Gas Limited                                                  30100201550  ...                             6501250500650900
Green Gas Limited                                                          42  ...                                       350150
Gujarat Gas Limited                                                         4  ...                                           55
Hindustan Petroleum Corporation Limited                                    38  ...                                         1183
IRM Energy Private Limited                                                 35  ...                                          188
Indian Oil Corporation Limited                                 12997182731585  ...                     800130040095025001368520
IndianOil-Adani Gas Private Limited                    4645142130125200462480  ...              1304-92716711103212616626802230
Indraprastha Gas Limited                                                   36  ...                                         1755
Maharashtra Natural Gas Limited                                       3715625  ...                                   3542181759
Megha Engineering & Infrastructures Limited                         121211075  ...                               80080020201500
Torrent Gas Private Limited                            4527541322722254273627  ...      318649526101203033936666507616025814792
Tripura Natural Gas Company Limited                                        66  ...                                        17060
Unison Enviro Private Limited                                            4230  ...                                         7510

[22 rows x 3 columns]
>>> dg.dtypes
GA Id                            object
GA Name                          object
State                            object
Winning Entity                   object
Network\rTariff\r(Rs/MMBTU)     float64
Compression\rCharge\r(Rs/kg)    float64
CNGStations                      object
PNGConnections                   object
SteelPipe                        object
dtype: object
>>> dg.reset_index(drop=True,inplace=True)
>>> dg
    GA Id                                            GA Name  ...    PNGConnections              SteelPipe
0     NaN                                                NaN  ...  PNG\rConnections  Steel Pipe\r(Inch-km)
1    GA_2           Cachar, Hailakandi & Karimganj Districts  ...             95001                    751
2    GA_3             Kamrup & Kamrup Metropolitan Districts  ...            321001                    961
3    GA_4              Aurangabad, Kaimur & Rohtas Districts  ...             14271                    800
4    GA_5                                 Begusarai District  ...            169787                    762
..    ...                                                ...  ...               ...                    ...
82  GA_83  Moradabad (Except areas already authorized)\rD...  ...            154800                    792
83  GA_84           Unnao ( Except areas already authorized)  ...              3000                    150
84  GA_85                                  Dehradun District  ...            300001                    900
85  GA_86                                   Burdwan District  ...            247852                   2230
86  4,346                                        2,10,48,045  ...               NaN                    NaN

[87 rows x 9 columns]
>>> dg.drop(index=86,inplace=True)
>>> dg
    GA Id                                            GA Name  ...    PNGConnections              SteelPipe
0     NaN                                                NaN  ...  PNG\rConnections  Steel Pipe\r(Inch-km)
1    GA_2           Cachar, Hailakandi & Karimganj Districts  ...             95001                    751
2    GA_3             Kamrup & Kamrup Metropolitan Districts  ...            321001                    961
3    GA_4              Aurangabad, Kaimur & Rohtas Districts  ...             14271                    800
4    GA_5                                 Begusarai District  ...            169787                    762
..    ...                                                ...  ...               ...                    ...
81  GA_82  Meerut (Except areas already authorized),\rMuz...  ...            105543                   1755
82  GA_83  Moradabad (Except areas already authorized)\rD...  ...            154800                    792
83  GA_84           Unnao ( Except areas already authorized)  ...              3000                    150
84  GA_85                                  Dehradun District  ...            300001                    900
85  GA_86                                   Burdwan District  ...            247852                   2230

[86 rows x 9 columns]
>>> dg.drop(index=0,inplace=True)
>>> dg
    GA Id                                            GA Name          State  ... CNGStations  PNGConnections  SteelPipe
1    GA_2           Cachar, Hailakandi & Karimganj Districts          Assam  ...          21           95001        751
2    GA_3             Kamrup & Kamrup Metropolitan Districts          Assam  ...          51          321001        961
3    GA_4              Aurangabad, Kaimur & Rohtas Districts          Bihar  ...          12           14271        800
4    GA_5                                 Begusarai District          Bihar  ...          25          169787        762
5    GA_6                           Gaya & Nalanda Districts          Bihar  ...          46           37591       1304
..    ...                                                ...            ...  ...         ...             ...        ...
81  GA_82  Meerut (Except areas already authorized),\rMuz...  Uttar Pradesh  ...          36          105543       1755
82  GA_83  Moradabad (Except areas already authorized)\rD...  Uttar Pradesh  ...          27          154800        792
83  GA_84           Unnao ( Except areas already authorized)  Uttar Pradesh  ...           2            3000        150
84  GA_85                                  Dehradun District    Uttarakhand  ...          50          300001        900
85  GA_86                                   Burdwan District    West Bengal  ...          80          247852       2230

[85 rows x 9 columns]
>>> dg.PNGConnections.apply(pd.to_numeric,errors='coerce').isnull().any()
True
>>> dg.SteelPipe.apply(pd.to_numeric,errors='coerce').isnull().any()
True
>>> dg.loc[1,'PNGConnections']
'95001'
>>> pd.to_numeric(dg['PNGConnections'], errors='coerce')
1      95001.0
2     321001.0
3      14271.0
4     169787.0
5      37591.0
        ...
81    105543.0
82    154800.0
83      3000.0
84    300001.0
85    247852.0
Name: PNGConnections, Length: 85, dtype: float64
>>> pd.to_numeric(dg['PNGConnections'], errors='coerce').isna()
1     False
2     False
3     False
4     False
5     False
      ...
81    False
82    False
83    False
84    False
85    False
Name: PNGConnections, Length: 85, dtype: bool
>>> pd.to_numeric(dg['PNGConnections'], errors='coerce').isna().sum()
3
>>> dg[pd.to_numeric(dg['PNGConnections'], errors='coerce').isna()]
   GA Id GA Name State  ...    CNGStations    PNGConnections              SteelPipe
23   NaN     NaN   NaN  ...  CNG\rStations  PNG\rConnections  Steel Pipe\r(Inch-km)
48   NaN     NaN   NaN  ...  CNG\rStations  PNG\rConnections  Steel Pipe\r(Inch-km)
70   NaN     NaN   NaN  ...  CNG\rStations  PNG\rConnections  Steel Pipe\r(Inch-km)

[3 rows x 9 columns]
>>> dg.drop(index=[23,48,70],inplace=True)
>>> dg.reset_index(drop=True,inplace=True)
>>> pd.to_numeric(dg['PNGConnections'], errors='coerce')
0      95001
1     321001
2      14271
3     169787
4      37591
       ...
77    105543
78    154800
79      3000
80    300001
81    247852
Name: PNGConnections, Length: 82, dtype: int64
>>> dg['PNGConnections']=pd.to_numeric(dg['PNGConnections'], errors='coerce')
>>> dg.dtypes
GA Id                            object
GA Name                          object
State                            object
Winning Entity                   object
Network\rTariff\r(Rs/MMBTU)     float64
Compression\rCharge\r(Rs/kg)    float64
CNGStations                      object
PNGConnections                    int64
SteelPipe                        object
dtype: object
>>> dg['CNGStations']=pd.to_numeric(dg['CNGStations'], errors='coerce')
>>> dg['SteelPipe']=pd.to_numeric(dg['SteelPipe'], errors='coerce')
>>> dg.dtypes
GA Id                            object
GA Name                          object
State                            object
Winning Entity                   object
Network\rTariff\r(Rs/MMBTU)     float64
Compression\rCharge\r(Rs/kg)    float64
CNGStations                       int64
PNGConnections                    int64
SteelPipe                       float64
dtype: object
>>> dg.groupby('Winning Entity')['CNGStations','PNGConnections','SteelPipe'].sum()
__main__:1: FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.
                                                    CNGStations  PNGConnections  SteelPipe
Winning Entity
AG&P LNG Marketing Pte. Ltd.                                111         1151111      668.0
Adani Gas Limited                                           452         2362544    10555.0
Bharat Gas Resources Limited                                297         1274049    11657.0
Consortium of AG&P LNG Marketing Pte Ltd.\r& At...           91          592422      251.0
Consortium of Assam Gas Company Limited,\rOil I...           72          416002     1712.0
Consortium of Haryana City Gas Kapil Chopra\rEn...           46          251370     1991.0
Consortium of SKN Haryana City Gas\rDistributio...          130          275000     2100.0
Consortium of Think Gas Investments PTE\rLimited            129          720009     3270.0
Essel Gas Company Limited                                    14           18000      412.0
GAIL Gas Limited                                            215          851001     3950.0
Green Gas Limited                                             6            7000      500.0
Gujarat Gas Limited                                           4            1750       55.0
Hindustan Petroleum Corporation Limited                      38           98000     1183.0
IRM Energy Private Limited                                   35           91000      188.0
Indian Oil Corporation Limited                              572         1361660     7838.0
IndianOil-Adani Gas Private Limited                         838         2246836    11703.0
Indraprastha Gas Limited                                     36          105543     1755.0
Maharashtra Natural Gas Limited                             218         1076859     3294.0
Megha Engineering & Infrastructures Limited                 209          964998     5120.0
Torrent Gas Private Limited                                 651         6207114    41664.0
Tripura Natural Gas Company Limited                          12           27314      230.0
Unison Enviro Private Limited                                72          110999       85.0
>>> dg.groupby('Winning Entity')['CNGStations','PNGConnections','SteelPipe'].count()
__main__:1: FutureWarning: Indexing with multiple keys (implicitly converted to a tuple of keys) will be deprecated, use a list instead.
                                                    CNGStations  PNGConnections  SteelPipe
Winning Entity
AG&P LNG Marketing Pte. Ltd.                                  1               1          1
Adani Gas Limited                                            13              13         13
Bharat Gas Resources Limited                                 11              11         10
Consortium of AG&P LNG Marketing Pte Ltd.\r& At...            2               2          1
Consortium of Assam Gas Company Limited,\rOil I...            2               2          2
Consortium of Haryana City Gas Kapil Chopra\rEn...            1               1          1
Consortium of SKN Haryana City Gas\rDistributio...            1               1          1
Consortium of Think Gas Investments PTE\rLimited              2               2          2
Essel Gas Company Limited                                     1               1          1
GAIL Gas Limited                                              5               5          5
Green Gas Limited                                             2               2          2
Gujarat Gas Limited                                           1               1          1
Hindustan Petroleum Corporation Limited                       1               1          1
IRM Energy Private Limited                                    1               1          1
Indian Oil Corporation Limited                                7               7          7
IndianOil-Adani Gas Private Limited                           9               9          8
Indraprastha Gas Limited                                      1               1          1
Maharashtra Natural Gas Limited                               3               3          3
Megha Engineering & Infrastructures Limited                   4               4          4
Torrent Gas Private Limited                                  10              10         10
Tripura Natural Gas Company Limited                           2               2          2
Unison Enviro Private Limited                                 2               2          2
>>> driver = webdriver.Chrome()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'webdriver' is not defined
>>>  