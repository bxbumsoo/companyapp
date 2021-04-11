from django.shortcuts import render

# Create your views here.

list_name = ['A0', 'A1', 'B0', 'B1', 'C0', 'C1', 'D0', 'D1', 'E0', 'E1', 'F0', 'F1', 'G0', 'G1', 'H0', 'H1', 'H2', 'H3', 'I0', 'I1',
             'J0', 'J1', 'K0', 'K1', 'L0', 'L1', 'M0', 'M1', 'N0', 'O0', 'P0', 'B1', 'B2', 'ez5', 'ez4', 'ez3', 'ez2', 'ez1', 'ezb1', 'dajl', 'dajr']

A0 = ['4303TX', '4301HDP', '753DCU3', 'DC101P', 'DC204PU', 'G2', '407NEC LP', '122LAMP-WC', 'BT203RM', 'BT029TRM', '435TC', '625U3', 'RS232 2P', '854DCU3',
      '1611SPO', '1615SP', '535TC', 'X1 MINI(W)', 'x1 mini(B)', '4302HDVP', '405NEC LP', '116LAMP', '120LAMP', '121LAMP-C', '415M U3', '236CPS(B)', '236CPS(W)']
A1 = ['504N', 'RS232SC30', 'RS232U30', '322TCC', '1615SP', '340PL', 'US485C01', '341PL-SC',
      '001HDGL', '04P RAID', 'EOC302POE', 'RS232-TC', 'US485C01', '1603SP', '323TCA']
B0 = ['1405HD4K', '2002UHD4K', '1410HD4K', '2005UHD4K', '1415HD4K', '1403HD4K', '12020HD4K', '28018HD4K', '2005UHD4K', '010UHD4K', '050UHD4K', '2020UHD4K', '020UHD4K', 'SFP1G-LX-SM', '100UHD4K', '1010HDCA', '28018UHD8K', '28015UHD8K', '020UHD4K', '1005HDCA', '1003HDCA', '1002HDCA', '42485LP2 EX', '42485LP4 EX',
      '1420HD4K', 'DVI200', 'DVI015', 'SFP10G-SR', 'SFP1G-CP', '150UHD4K', '12015HD4K', 'EC232485 2P', '2010UHD4K', '015UHD4K', 'SC101', '1011HDCA', '030UHD4K', '28030UHD4K', '1430HD4K', '14015HD4K', '1402HD4K', '952EX OXFORD', 'SFP1GDT-SX-MM', '2003UHD4K', '20015UHD4K', '2001UHD4K', 'DVI030', '954LP EX']
B1 = ['201CA', '364DCP EX', '111TCE', '201PL EX', '362DCP EX', '1101TC', 'TC313LAN', 'RGB300', '1200AC', '361DCP EX', '1284PL', '1394VT EX', '1394TI', '1000K EX', '551CP-10G', '1000K LP', '2005GH', '540CP-10G', '1900AC', '110EA', 'RGB050', 'RGB020',
      '462DCP EX', '542SFP-10G', '220TC', '220UL', '360DCP EX', '1000K LP', '3100K EX', 'RGB100', '351SFP-1G', '1100U3', 'POE2302EX4', 'RGB150', '915V3', '550CP-10G', '210CA', '2501GU3', 'TC343LAN', '561SFP-10G', 'RGB200', '1202AC-AP']
C0 = ['911FT', '2000GSCSW-A', '2000GSCSW-B', 'POE706EF', '8501POE', 'POE4803JM', 'PSE4809AT', '868LTT', '2000G-SFP', '400PT', 'POE810F-2TP', '478PT',
      '200FSCSW-B', '200FSCSW-A', '858LT', 'POE202EX', '2008SFP-TP', 'POE201EX', '2008SFP-TP', 'POE201EX', '488PDT', 'POE4805JM', 'POE4807J-60W']
C1 = ['3022SFP', 'PE844H', 'HTB515', 'POE1528GDT', 'PE4804J',
      'POE332SFP-TP', 'POE3108UL2-SFP', 'POE505F', 'HTB515', 'POE1001EX']
D0 = ['7402KVM-DUAL', '7402KVM-DUAL', '2212UHD4K', '4401SLS', '1008SP4K', '1026HFC-KVM', '4244HDM',
      '7104KVM EX', '2403UHDM', '1022HFC', '4248UHDM', 'HD150POC-4K60', '4245HDM', '1027HFC-4K60']
D1 = ['2431ST', '60HDC', '2416HVC-MN', '400HDW', '2602HDSC', '1608AHD', '502SK4K', '2101SDHC',
      'HD70RS-4K', 'SDI0102SP', '502SP4K', '512SP4K', '514SP4K', 'SDI0104SP']
E0 = ['313DPHU3', '2423VHC', '313DPHU3', '2232TCV', '2231TCH', '170HDC', '2252TCHV',
      '2246CHPD', '3405SW4K', '2233TCD', '326TCH-DX', '3412SW4K', '2251TCH', '2421HVC']
E1 = ['331TC-PD', '501AC', 'USB100', '14AC', '717UH', '414U3',
      '33QWC(B)', '503OTG', '415TC', '703U3NP', '704UH', '1568QLC', '707UHP', 'USB60', '1573LMM', 'USB105PW', '31WC-B', 'USB404']
F0 = ['204BT', 'HD301SWC4K', 'QTC613', '1403CHG', '10WC-PB(B)', '10WC-PB(W)', '3422BTC', '1413CHG', 'QTC605', '403SWC4K60', '8004FSC', '118WC-PD', '6003HW-PB', '1422BTC', '1545L8',
      '10007QPB', '005TC', '035RHD4K', '5005PBCB', 'BT20CST', '4202SPC4K', '2422BTC', '4202SPC4K', '5005PBCB', 'DVI202SW', '04AC', 'IDE JENDER', '10006TQPB', '20001QPB', '04AC-4P']
F1 = ['316TCH-PD', '9718U3', '411TCH', '9720TC-OTG', '318TCH-PD', 'M2280C5', '413TCH-DX', '240PSE', 'MTV340-4K', '840A', 'MTV310', '531WBT', 'MTV330-4K', '486TC', '2420HDP', '202N MINI',
      '9716TC-PD', '317TCH', '2244TCH', '9713TCU3', '8601U3', '9714TC', '2244TCH', '120PSE', '9717U2', '830A', '9712TC', '1300WBT', '9715TC-PD', 'BT22CSA', '8600CR', '9721TC', 'MTV320', '318TCH-PD']
G0 = ['315UH', 'JUD480', '505UH', '614U3', 'JUH377', '218SATAIDE NEW', 'RJ45', 'RJ45', '518U3 SATAIDE', 'TCA03EX', 'TCC03EX', '505UHP', 'JCA153',
      'JCA366', 'JEE256', 'JVCU100', '510UHP', '614U3', 'M 2281C', 'M2285U3', 'JCD543', 'JCA141', '214UH', 'UH104G', 'JCD381', '616TC', 'JCA379', '615TC']
G1 = ['JUA250', 'JUCX01', 'JDA159', 'JUC500', 'JUA365', 'JUC500', 'JUC100', 'JUA350',
      'JUCX10', 'JCH377', 'JDA112', 'JUE130', 'JUA254', 'JUC501', 'JTCX02', 'JDA134', 'JUC700']
H0 = ['1528LCMD', '2241TCH-WHITE', '2241TCH-BLACK', 'BT50GST', '1525L', '1533CC', '1512TC', '1521',
      'KVMPS2', '115CDP', '1513TC', '1516TC', 'PS2', '120TLC', '1517TC', '2412VHC', '2243TCV', '2411HVC', '1524M']
H1 = ['LL305MM-10G', 'LL310MM-10G', '2242TCD', 'LL203SM', 'LS203MM', 'LS201MM', 'LS203SM', 'SS203SM', 'LL203MM',
      '1518OTG-TC', 'LS330MM-10G', '1201AC', 'SS203MM', '1529LCMD', '1003M', 'LL201MM', 'LL201SM', 'LN00-QC3C']
H2 = ['204UH NEW', 'LL205SM', 'LS210SM', 'LL220SM', 'LS220SM', 'SS230SM', 'LL250MM', 'LL220MM',
      'SS230MM', 'LS230MM', 'SS220MM', 'SPT2015SM', 'LS230SM', 'LL210SM', 'SS205MM', 'SS250SM']
H3 = ['1642STC-Y', 'IPC-E3204S-B', '1651HDVI-MF', '1655VGA-FF', '1653RJC', 'DPA301D-00(5V1A허)', 'IPC-E2202SL-C', 'DPAS04H-00', 'DPA301D-00', '1652HDVI-FM', '1650HD-FF',
      '1547ST-MF', 'IPC-E2204S-B', '1542ST-MF', '1541ST-MF', '1554ST-MM', 'D2H13MD', 'UPD2018-B', '1543ST-MF', '1648PS2', '1647OTG', '1569-3RC', '1585ST-2RC']
I0 = ['659CCU3', '35HR', '351TCU3', '110LAMP', '350U3', '05AC', '7004N', '525U3', '651DCU3 HUB',
      '652DCU3', 'QC602', '8004N', '318U3', '418U3', '108LAMP', '650TC', '352U3', '109LAMP']
I1 = ['645U3', '804U3 RAID', '704TC', '852DCU3', '852DCU3', '962DCU3', '215U3', '200DVD-RW', '802U3 RAID', '101DVD-RW', '201DVD-COMBO', '200DVD-RW', '425U3',
      '100DVD-RW', '965TC', '952DCU3', '706M 6G', '702U3 RAID', '963DCU3H', '964DCU3C', '702TC RAID', '954DCU3', '644DU3', '706M6G', '802TC RAID', '110LAMP']
J0 = ['220V', '1204AC-AP', '2serial EX', '101DVD-COMBO', 'USB05', '9703U3', 'SL602 PCle', '1024GS', '1016GS', 'USB10', '1serial EX', '1026GSFP',
      'RS232U20', 'USB20', 'USB15', 'SL601 PCIE', 'RS232U20', '890AP-10K(+POE2403JM)', '305NEC EX', '1025GS IGMP', '200HCS', '206NEC EX', '212U3']
J1 = ['707U3', 'USB30PW', 'USB30U3', '408PB-UPS', 'UH303LAN', 'UH103LAN', '2000GSCM', '2016GS', '2000GSCS', 'USB10U3', '200FSCS', '6008GH', '6008GH-IGMP', '2200GU3', '2200GTC', 'USB05U3NP', '306UHP',
      'USB05 PLUS', 'UH305', 'UH308', '704U3', 'USB10U3PW', 'USB05U3NP', 'UH309PD', '208PB-UPS', '200FSCS', '314UHP', '964DCU3', '2024GS', '6005GH', '200FSCM', '8408SH', '316U3', '319U3', '704UHP']
K0 = ['7002KVM-4K', '7004KVM-4K', '2516VSP', '0102SPC4K', '7018KVM-KP', '100HDC', '122SDHC', '124HSDC', '2216VHC', '2215HVC', '405SW4K60', '0104SP4K', 'HD102SP4K', '402SP4K60', '2404VSW',
      '2216VHC', '622HC-KVM', '100HDCR', '7202KVM-4K', '2302VSP', '7014KVM-KP', '100HDCR', 'HD310SW4K', '404SP4K60', '2402VSW', '7012KVM-4K-PK', '0501SW4K', '2502VSP', 'HD104SP4K', '2304VSP', '7208KVM']
K1 = ['7008KVM', 'N80VE', '37QTC', '07AC', '3504PST', '7012KVM-KP',
      'HD108SP4K', '7204KVM-4K', '07AC', 'N200VE', '7102KVM-4K', 'N100VE',  '0226SP', '1411CHB', '1405CHB', '632DC-KVM', '612VC-KVM', '3502PST']
L0 = []
L1 = []
M0 = []
M1 = []
N0 = []
O0 = []
P0 = ['POE528TP-COMBO', '3028GL2-SFP', 'POE320SFP-PD', '3110GL2-SFP', '3029GL2-10G', 'POE3008GFJ1', 'POE328SFP-PD', '3029GL2-10G',
      '2052GL2-10G', 'POE306EF', '1018GS IGMP', 'POE510-TP', '1018GS IGMP', 'POE4808J-95W', 'POE7006SFP-TP', 'POE327SFP-TP', 'POE324SFP-TP']

JB1 = ['0102SP4K', '0102SPC4K', '0104SP4K', '0301SW4K', '0501SW4K', '05AC', '1000K EX', '1000K LP', '100DVD-RW', '100HDC', '1016GS', '1016GSFP', '1018GS-IGMP', '1019G-SF', '101DVD-COMBO', '1024GS', '104BT', '109LAMP', '120LAMP', '1422BTC', '1SEERIAL EX', '2016GS', '2024GS', '204BT', '218SATA NEW', '208PB-UPS', '215U3', '225SSD', '2402VSW', '2404VSW', '2422BTC', '2SERIAL EX', '304BT', '305NEC EX',
       '3422BTC', '3502PST', '3504PST', '35HR', '408PB-UPS', '415MU3', '425U3', '435TC', '515TC', '518U3', '525U3', '6005GH', '6005GH IGMP', '6008GH', '6008GH IGMP', '652DCU3', '702U3 RAID', '704UHP', '704U3', '706M6G', '8408SH', '852DCU3', '9703U3', 'AMH360', 'BT150CST', 'MOH360A', 'MTV302', 'MTV320', 'MTV330-4K', 'MTV340-4K', 'QC602', 'RS232U20', 'UH305', 'UH308', 'USB05', 'USB10', 'USB100', 'USB15', 'USB20']
JB2 = []

EZ5 = ['0226SP', '04P RAID', '10MM', '120PSE', '142VW', '1603SP', '16MM', '200HCS', '2101SDHC', '2102SDHC', '232RS16', '240PSE', '2516VSP', '2602HDSC', '4150VE', '42485LP', '42485LP2 EX', '42485LP4 EX', '604V2', '606N', '7004N', '708M6G', '8004N', '8024SH', '8316SH',
       '852LPP', '854LP', '915V3', '954LP EX', '958LP EX', '966LP EX', 'BT13CS', 'BT14SC', 'DC101P', 'DC102P', 'DC103P', 'DC204PU', 'EC232485 2P', 'EC232485 4P', 'F30', 'FC232485 CM', 'FC232485 CS', 'HD070IR', 'HD140TX-4K', 'HD141TX-4K', 'HD40SP-4R', 'RJ45', 'RJ45C6', 'SC101']
EZ4 = ['101PL', '006LED', '105NEC', '111TCE', '1284PL', '1300WBT', '1301DS-PD', '1302WBTA', '1394TI', '1394VT EX', '1601SP', '1603SP', '1606SP-P', '1SERIAL LP', '201PL EX', '212U3', '2212UHD4K', '2218VDHP', '2287TCH', '2420HDP', '2SERIAL LP', '3102D EX', '312DPVU3', '315UH', '316U3', '319U3', '322TCC', '323TCA', '328TC', '329TC', '330TC', '338TC', '340PL', '341PL-SC', '342PL-TC', '3506PST',
       '35QTC', '405NEC LP', '407NEC LP', '448TC', '488PDT', '612VC-KVM', '622HC-KVM', '632DC-KVM', '715TC', '717UH', '722HC-KVM', '8100UHD-4KK', '8120UHD-4K', '952EX OXFORD', '9719TC-OTG', '9720TC-OTG', 'AV2301', 'AV2302', 'AV2303', 'AV2304', 'AV2307', 'HD60CAP-4K', 'IDE JENDER', 'KVMPS2', 'PS2', 'RS201SW', 'RS232 2P', 'RS232 4P', 'RS232SC', 'RS232SC30', 'RS232U30', 'SL601PCIe', 'SL602PCIe', 'UH309PD']
EZ3 = ['001TC', '005TC', '006TC-4P', '007TC-PD', '008TC-5P', '1100CA', '1100U3', '1101TC', '110EA', '1541ST', '1542ST', '1543ST-MF', '1547ST', '1550ST-MM', '1551ST', '1554ST', '1555ST', '1556ST', '1557ST-MM', '1569ST-3RC', '1585ST', '160CC', '202N mini', '204UH NEW', '210CA', '214UH', '2200GTC', '2200GU3', '220TC', '220UL', '300N mini', '306UHP', '313DPHU3', '314UH', '314UHP', '316TCH-PD', '324UH', '325GEN32', '326TCH-DX', '331TC-PD', '413TCH-DX', '414U3', '415TC', '468LT', '478PT', '495UCG', '501AC', '503OTG', '505UH', '505UHP', '506OTG', '510UHP', '513WBT', '535TC', '622HDT',
       '633DPT', '703U3', '704UH', '707UHP', '8501POE', '858LT', '8600CR', '8601POE', '8601U3', '8602TU3', '8603TCU3', '868LTT', '911FT', '9708U3', '9712TC', '9713TCU3', '9714TC', '9715TC-PD', '9717U2', '9718U3', '9721TC', 'M2280C5', 'M2281C', 'M2283TCA', 'M2284NVME', 'M2285U3', 'M2286-COMBO', 'M2289NVME-G32', 'RS232S5', 'RS232TC', 'TC313LAN', 'TC343LAN', 'TCA03EX', 'TCA05EX', 'TCC03EX', 'TCC05EX', 'UH103LAN', 'UH104G', 'UH303LAN', 'USB05PLUS', 'USB05U3', 'USB105', 'USB105PW', 'USB10U3', 'USB15U3', 'USB190', 'USB20U3', 'USB30PW', 'USB30U3', 'USB404', 'USB40U3PW', 'USB60', 'X1 MINI']
EZ2 = ['04AC', '04AC-4P', '07AC', '10001PB', '10005QPB', '10006TQPB', '10007QPB', '10MM', '10WC-PB', '118WC-PB', '1403CHG', '1406CHG', '1407CHG', '1413CHG', '1429CH', '14AC', '1512TC', '1516TC', '1517TC', '1518OTG-TC', '1521TM', '1522KLM', '1523KCM', '1524M', '1525L', '1526C', '1527LM', '1528LCMD', '1529LCMD', '1530M', '1531L', '1532C', '1533CC', '1534M5', '1535L8', '1536C', '1544M5', '1545L8', '1546C', '1565QMC', '1567QTC', '1568QLC', '1573LMM', '20001QPB', '280S3', '318U3', '31WC', '32QWC', '33QWC', '351TCU3', '352SU',
       '352U3', '353C', '37QTC', '412U3', '418U3', '47QTC', '5000PB', '5005PBCB', '6000HW-PB', '6003HW-PB', '618DEU3', '625U3', '644DU3', '645U3', '650TC', '651DCU3 HUB', '653DC', '659CCU3', '702TC', '704TC', '753DCU3', '766FP', '8004FSC', '802TC', '802U3', '804U3', '820A', '830A', '840A', '854DCU3', '954DCU3', '962DCU3', '963DCU3H', '964DCU3C', '965TC', 'BT026TRM', 'BT029TRM', 'BT16C', 'BT18CS', 'BT20CST', 'BT22CSA', 'BT23CSM', 'BT50GST', 'G2', 'K380BT', 'Q3', 'QTC601', 'QTC603', 'QTC604NB', 'QTC605', 'QTC613', 'SWP3500']
EZ1 = ['1005POE', '1008POE', '1052SFP-10G', '2000FSCM', '2000GSCS', '2000GSCS-PW', '2000G-SFP', '2001POE-SFP', '2002SFP-10G', '2008SFP-TP', '200FSCM', '200FSCSW-B', '2052GL2-10G', '2201SFP', '236CPS', '2424DVC', '2425VDC', '2500K EX', '2501GU3', '2502GTC', '300FSCM-POE', '300FSCSWA-POE', '300FSCSWB-POE', '3011SFP', '3022SFP', '3028GL2-SFP', '3029GL2-10G', '3032FGL2-SFP', '3110GL2-SFP', '3229GL2-10G', '4028L3-10G', '4028L3-10G', '4052L3-10G', '4302HDP', '4504HDP', '4516HDP', '4604VPS-36V', '4608VPS-36V', '4616VPS-36V', '506POE-TP', '510POE-TP', '57QWC', '614U3', '615TC', '616TC', '815V3', '8305SH', 'EOC201THD', 'EOC208THD', 'EOC302POE',
       'EOC304POE(RX)', 'EOC304POE(TX)', 'HD150POC-4K60', 'HD50POC-4K60', 'HTB515', 'PE4804J', 'PE844H', 'PEG4806JT', 'POE101EX', 'POE1524GDT', 'POE1528GDT', 'POE1616FG', 'POE1620L2-300', 'POE19ST', 'POE2001EXW', 'POE2002EXW', 'POE201EX', 'POE202EX', 'POE2067EXW', 'POE2403JM', 'POE2406AU-240', 'POE2418LED-PM', 'POE2424SFP-380', 'POE2428LED-PM', 'POE2429L2-370', 'POE2430L2-380', 'POE2610MDT', 'POE2812AU-240', 'POE3004PD', 'POE3004PD-60', 'POE3005GF', 'POE3008GF', 'POE3008LED-120', 'POE3010G-2TP', 'POE3018SFP-250', 'POE3020SFP', 'POE3026SFP-400', 'POE306EF', 'POE308SFP-TP-V3', 'POE3108UL2-SFP', 'POE310F-2TP', 'POE316SFP-TP', 'POE318SFP-TP', 'POE320SFP-PD', 'POE322SFP-TP', 'POE324SFP-TP', 'POE327SFP-TP', 'POE332SFP-TP', 'POE4010L2-140', 'POE4012L2-SFP', 'POE4018LED-240', 'POE4028L2S-TP', 'POE4110L2-SFP', 'POE4210L2S-TP', 'POE4803JM', 'POE4805JM', 'POE4807J-60W', 'POE4808J-95W', 'POE505F', 'POE524FDT', 'POE6005F', 'POE6008F', 'POE605F', 'POE606F', 'POE608F', 'POE7006SFP-TP', 'POE706EF', 'POE808FP', 'POE810F', 'PSE4809AT', 'QTC611']
EZB1 = ['001HDGL', '0301SWC4K', '030IR', '035RHD4K', '1008SP', '1021VFC', '1022HFC', '1023DFC', '1025SFC', '1026HFC-KVM',
        '1027HFC-KVM', '1027HFC-4K60', '102DVI', '1030HDFC', '104DVI', '1050HDFC', '1080HDFC', '1100HDFC', '112CMDP', '112DVI-EDID', '113CDP', '114DVI-EDID', '1150HDFC', '115CDPP', '1200AC', '1200HDFC', '1201AC', '1202AC-AP', '120TLC', '122SDHC', '124HSDC', '1300HDFC', '1394B EX', '1404CHG', '1408QTC', '1508A', '170HDC', '170HDCR', '1900AC', '2202HDM', '2215HVC', '2216VHC', '2217HDAV', '2231TCH', '2232TCV', '2242TCD', '2243TCV', '2244TCH', '2245CHPD', '2246CHPD', '2251TCH', '2261TCH-DUAL', '2271TCH-4K', '2273TCH-4K', '2302VSP', '2304VSP', '2402HDM', '2404HDM', '2411HVC', '2412VHC', '2415HVC', '2416HVC-MN', '2417HVC-MR', '2418VHC', '2421HVC', '2423VHC', '2502VSP', '2504VSP', '2508VSP', '270WIP', '270WIP-R', '310HST', '311TCH', '317TCH', '318TCH-PD', '334N-AP', '3403SW4K', '3412SW4K', '351SFP-1G', '352SFP-1G', '360DCP EX', '361DCP EX', '362DCP EX', '364DCP EX', '400HDW', '400HDW-R', '402SP4K60', '402SPC4K60', '403SW4K60', '403SWC4K60', '404SP4K60', '405SW4K60', '408SP4K60', '411TCH', '412TCV', '416TCH-DX', '4202SPC4K', '4244HDM', '4245HDM', '4246HDM', '4248UHDM', '4288UHDM', '4301HDP', '4303TX', '4308HDVP', '4309HDVP-C', '4401SLS', '4404SLS', '4405SMW', '462DCP EX', '50HDC', '50SR', '512SP4K', '514SP4K', '60HDC', '7002KVM', '7004KVM', '7008KVM', '7016KVM', '7104KVM', '7202KVM', '7204KVM', '7208KVM', '7216KVM', '7402KVM-DUAL', '7460KVM EX', '890AP-10K', 'BT203RM', 'DL303U3D', 'DP102VS', 'DVI050TR', 'DVI202SW', 'EOC302POE', 'EOC7002', 'HD100RS-4K', 'HD102SP4K', 'HD104SP4K', 'HD108SP4K', 'HD116SP4K', 'HD301SW', 'HD301SW4K', 'HD301SWC4K', 'HD501SW', 'HD501SW4K', 'HD70RS-4K']


DAJL = ['122LAMP-WC', '10BCR', '116MLAMP', '1204AC-AP', '1402CHB',
        '1405CHB', '1410WC-C', '1411CHB', '1419FAN', '1421FAN(KP쏠)', '675PB']
DAJR = ['108LAMP', '1412FAN', 'BT15C', '1418FAN',
        '1428FAN-T(KP쏠)', '1025GS IGMP', '3024GL2-SFP', '121LAMP-C', '14GDP', '1005GH', 'BT30CST']


def search(request):
    message = request.GET.get('message')       # 검색 품목 받기
    info = request.GET.get('info')       # 제품 위치

    resultA0 = []
    resultA1 = []
    resultB0 = []
    resultB1 = []
    resultC0 = []
    resultC1 = []
    resultD0 = []
    resultD1 = []
    resultE0 = []
    resultE1 = []
    resultF0 = []
    resultF1 = []
    resultG0 = []
    resultG1 = []
    resultH0 = []
    resultH1 = []
    resultH2 = []
    resultH3 = []
    resultI0 = []
    resultI1 = []
    resultJ0 = []
    resultJ1 = []
    resultK0 = []
    resultK1 = []
    resultL0 = []
    resultL1 = []
    resultM0 = []
    resultM1 = []
    resultN0 = []
    resultO0 = []
    resultP0 = []

    if message:
        for itemA0 in A0:                   # for문으로 입력어가 포함된 품목 리스트에 담기
            if message.upper() in itemA0:
                resultA0.append(itemA0)
        for itemA1 in A1:
            if message.upper() in itemA1:
                resultA1.append(itemA1)
        for itemB0 in B0:
            if message.upper() in itemB0:
                resultB0.append(itemB0)
        for itemB1 in B1:
            if message.upper() in itemB1:
                resultB1.append(itemB1)
        for itemC0 in C0:
            if message.upper() in itemC0:
                resultC0.append(itemC0)
        for itemC1 in C1:
            if message.upper() in itemC1:
                resultC1.append(itemC1)
        for itemD0 in D0:
            if message.upper() in itemD0:
                resultD0.append(itemD0)
        for itemD1 in D1:
            if message.upper() in itemD1:
                resultD1.append(itemD1)
        for itemE0 in E0:
            if message.upper() in itemE0:
                resultE0.append(itemE0)
        for itemE1 in E1:
            if message.upper() in itemE1:
                resultE1.append(itemE1)
        for itemF0 in F0:
            if message.upper() in itemF0:
                resultF0.append(itemF0)
        for itemF1 in F1:
            if message.upper() in itemF1:
                resultF1.append(itemF1)
        for itemG0 in G0:
            if message.upper() in itemG0:
                resultG0.append(itemG0)
        for itemG1 in G1:
            if message.upper() in itemG1:
                resultG1.append(itemG1)
        for itemH0 in H0:
            if message.upper() in itemH0:
                resultH0.append(itemH0)
        for itemH1 in H1:
            if message.upper() in itemH1:
                resultH1.append(itemH1)
        for itemH2 in H2:
            if message.upper() in itemH2:
                resultH2.append(itemH2)
        for itemH3 in H3:
            if message.upper() in itemH3:
                resultH3.append(itemH3)
        for itemI0 in I0:
            if message.upper() in itemI0:
                resultI0.append(itemI0)
        for itemI1 in I1:
            if message.upper() in itemI1:
                resultI1.append(itemI1)
        for itemJ0 in J0:
            if message.upper() in itemJ0:
                resultJ0.append(itemJ0)
        for itemJ1 in J1:
            if message.upper() in itemJ1:
                resultJ1.append(itemJ1)
        for itemK0 in K0:
            if message.upper() in itemK0:
                resultK0.append(itemF1)
        for itemK1 in K1:
            if message.upper() in itemK1:
                resultK1.append(itemK1)
        for itemL0 in L0:
            if message.upper() in itemL0:
                resultL0.append(itemL0)
        for itemL1 in L1:
            if message.upper() in itemL1:
                resultL1.append(itemL1)
        for itemM0 in M0:
            if message.upper() in itemM0:
                resultM0.append(itemM0)
        for itemM1 in M1:
            if message.upper() in itemM1:
                resultM1.append(itemM1)
        for itemN0 in N0:
            if message.upper() in itemN0:
                resultN0.append(itemN0)
        for itemO0 in O0:
            if message.upper() in itemO0:
                resultO0.append(itemO0)
        for itemP0 in P0:
            if message.upper() in itemP0:
                resultP0.append(itemP0)

        if int(bool(resultA0))+int(bool(resultA1)) + int(bool(resultB0))+int(bool(resultB1))+int(bool(resultC0))+int(bool(resultC1))+int(bool(resultD0))+int(bool(resultD1))+int(bool(resultE0))+int(bool(resultE1))+int(bool(resultF0))+int(bool(resultF1))+int(bool(resultG0))+int(bool(resultG1))+int(bool(resultH0))+int(bool(resultH1))+int(bool(resultH2))+int(bool(resultH3))+int(bool(resultI0))+int(bool(resultI1))+int(bool(resultJ0))+int(bool(resultJ1))+int(bool(resultK0))+int(bool(resultK1))+int(bool(resultL0))+int(bool(resultL1))+int(bool(resultM0))+int(bool(resultM1))+int(bool(resultN0))+int(bool(resultO0))+int(bool(resultP0)) >= 2:    #
            return render(request, 'jinsung.html', {'many': '<검색 된 물품이 너무 많습니다. 좀 더 구체적으로 입력해주세요.>'})
        elif resultA0:
            return render(request, 'jinsung.html', {'A0': '♣', '검색어A0': '검색어 : ', 'ojA0': message, 'A0전체': 'A0 : ', 'resultA0': resultA0})
        elif resultA1:
            return render(request, 'jinsung.html', {'A1': '♣', '검색어A1': '검색어 : ', 'ojA1': message, 'A1전체': 'A1 : ', 'resultA1': resultA1})
        elif resultB0:
            return render(request, 'jinsung.html', {'B0': '♣', '검색어B0': '검색어 : ', 'ojB0': message, 'B0전체': 'B0 : ', 'resultB0': resultB0})
        elif resultB1:
            return render(request, 'jinsung.html', {'B1': '♣', '검색어B1': '검색어 : ', 'ojB1': message, 'B1전체': 'B1 : ', 'resultB1': resultB1})
        elif resultC0:
            return render(request, 'jinsung.html', {'C0': '♣', '검색어C0': '검색어 : ', 'ojC0': message, 'C0전체': 'C0 : ', 'resultC0': resultC0})
        elif resultC1:
            return render(request, 'jinsung.html', {'C1': '♣', '검색어C1': '검색어 : ', 'ojC1': message, 'C1전체': 'C1 : ', 'resultC1': resultC1})
        elif resultD0:
            return render(request, 'jinsung.html', {'D0': '♣', '검색어D0': '검색어 : ', 'ojD0': message, 'D0전체': 'D0 : ', 'resultD0': resultD0})
        elif resultD1:
            return render(request, 'jinsung.html', {'D1': '♣', '검색어D1': '검색어 : ', 'ojD1': message, 'D1전체': 'D1 : ', 'resultD1': resultD1})
        elif resultE0:
            return render(request, 'jinsung.html', {'E0': '♣', '검색어E0': '검색어 : ', 'ojE0': message, 'E0전체': 'E0 : ', 'resultE0': resultE0})
        elif resultE1:
            return render(request, 'jinsung.html', {'E1': '♣', '검색어E1': '검색어 : ', 'ojE1': message, 'E1전체': 'E1 : ', 'resultE1': resultE1})
        elif resultF0:
            return render(request, 'jinsung.html', {'F0': '♣', '검색어F0': '검색어 : ', 'ojF0': message, 'F0전체': 'F0 : ', 'resultF0': resultF0})
        elif resultF1:
            return render(request, 'jinsung.html', {'F1': '♣', '검색어F1': '검색어 : ', 'ojF1': message, 'F1전체': 'F1 : ', 'resultF1': resultF1})
        elif resultG0:
            return render(request, 'jinsung.html', {'G0': '♣', '검색어G0': '검색어 : ', 'ojG0': message, 'G0전체': 'G0 : ', 'resultG0': resultG0})
        elif resultG1:
            return render(request, 'jinsung.html', {'G1': '♣', '검색어G1': '검색어 : ', 'ojG1': message, 'G1전체': 'G1 : ', 'resultG1': resultG1})
        elif resultH0:
            return render(request, 'jinsung.html', {'H0': '♣', '검색어H0': '검색어 : ', 'ojH0': message, 'H0전체': 'H0 : ', 'resultH0': resultH0})
        elif resultH1:
            return render(request, 'jinsung.html', {'H1': '♣', '검색어H1': '검색어 : ', 'ojH1': message, 'H1전체': 'H1 : ', 'resultH1': resultH1})
        elif resultH2:
            return render(request, 'jinsung.html', {'H2': '♣', '검색어H2': '검색어 : ', 'ojH2': message, 'H2전체': 'H2 : ', 'resultH2': resultH2})
        elif resultH3:
            return render(request, 'jinsung.html', {'H3': '♣', '검색어H3': '검색어 : ', 'ojH3': message, 'H3전체': 'H3 : ', 'resultH3': resultH3})
        elif resultI0:
            return render(request, 'jinsung.html', {'I0': '♣', '검색어I0': '검색어 : ', 'ojI0': message, 'I0전체': 'I0 : ', 'resultI0': resultI0})
        elif resultI1:
            return render(request, 'jinsung.html', {'I1': '♣', '검색어I1': '검색어 : ', 'ojI1': message, 'I1전체': 'I1 : ', 'resultI1': resultI1})
        elif resultJ0:
            return render(request, 'jinsung.html', {'J0': '♣', '검색어J0': '검색어 : ', 'ojJ0': message, 'J0전체': 'J0 : ', 'resultJ0': resultJ0})
        elif resultJ1:
            return render(request, 'jinsung.html', {'J1': '♣', '검색어J1': '검색어 : ', 'ojJ1': message, 'J1전체': 'J1 : ', 'resultJ1': resultJ1})
        elif resultK0:
            return render(request, 'jinsung.html', {'K0': '♣', '검색어K0': '검색어 : ', 'ojK0': message, 'K0전체': 'K0 : ', 'resultK0': resultK0})
        elif resultK1:
            return render(request, 'jinsung.html', {'K1': '♣', '검색어K1': '검색어 : ', 'ojK1': message, 'K1전체': 'K1 : ', 'resultK1': resultK1})
        elif resultL0:
            return render(request, 'jinsung.html', {'L0': '♣', '검색어L0': '검색어 : ', 'ojL0': message, 'L0전체': 'L0 : ', 'resultL0': resultL0})
        elif resultL1:
            return render(request, 'jinsung.html', {'L1': '♣', '검색어L1': '검색어 : ', 'ojL1': message, 'L1전체': 'L1 : ', 'resultL1': resultL1})
        elif resultM0:
            return render(request, 'jinsung.html', {'M0': '♣', '검색어M0': '검색어 : ', 'ojM0': message, 'M0전체': 'M0 : ', 'resultM0': resultM0})
        elif resultM1:
            return render(request, 'jinsung.html', {'M1': '♣', '검색어M1': '검색어 : ', 'ojM1': message, 'M1전체': 'M1 : ', 'resultM1': resultM1})
        elif resultN0:
            return render(request, 'jinsung.html', {'N0': '♣', '검색어N0': '검색어 : ', 'ojN0': message, 'N0전체': 'N0 : ', 'resultN0': resultN0})
        elif resultO0:
            return render(request, 'jinsung.html', {'O0': '♣', '검색어O0': '검색어 : ', 'ojO0': message, 'O0전체': 'O0 : ', 'resultO0': resultO0})
        elif resultP0:
            return render(request, 'jinsung.html', {'P0': '♣', '검색어P0': '검색어 : ', 'ojP0': message, 'P0전체': 'P0 : ', 'resultP0': resultP0})
        else:
            return render(request, 'jinsung.html', {'검색어0': '검색어 : ', 'oj0': message, 'None0': '는(은) 없는 제품입니다.'})

    if info == 'A0':
        return render(request, 'jinsung.html', {'진성A0': '진성A0 : ', 'A0all': A0, 'A0': '♣'})
    elif info == 'A1':
        return render(request, 'jinsung.html', {'진성A1': '진성A1 : ', 'A1all': A1, 'A1': '♣'})
    elif info == 'B0':
        return render(request, 'jinsung.html', {'진성B0': '진성B0 : ', 'B0all': B0, 'B0': '♣'})
    elif info == 'B1':
        return render(request, 'jinsung.html', {'진성B1': '진성B1 : ', 'B1all': B1, 'B1': '♣'})
    elif info == 'C0':
        return render(request, 'jinsung.html', {'진성C0': '진성C0 : ', 'C0all': C0, 'C0': '♣'})
    elif info == 'C1':
        return render(request, 'jinsung.html', {'진성C1': '진성C1 : ', 'C1all': C1, 'C1': '♣'})
    elif info == 'D0':
        return render(request, 'jinsung.html', {'진성D0': '진성D0 : ', 'D0all': D0, 'D0': '♣'})
    elif info == 'D1':
        return render(request, 'jinsung.html', {'진성D1': '진성D1 : ', 'D1all': D1, 'D1': '♣'})
    elif info == 'E0':
        return render(request, 'jinsung.html', {'진성E0': '진성E0 : ', 'E0all': E0, 'E0': '♣'})
    elif info == 'E1':
        return render(request, 'jinsung.html', {'진성E1': '진성E1 : ', 'E1all': E1, 'E1': '♣'})
    elif info == 'F0':
        return render(request, 'jinsung.html', {'진성F0': '진성F0 : ', 'F0all': F0, 'F0': '♣'})
    elif info == 'F1':
        return render(request, 'jinsung.html', {'진성F1': '진성F1 : ', 'F1all': F1, 'F1': '♣'})
    elif info == 'G0':
        return render(request, 'jinsung.html', {'진성G0': '진성G0 : ', 'G0all': G0, 'G0': '♣'})
    elif info == 'G1':
        return render(request, 'jinsung.html', {'진성G1': '진성G1 : ', 'G1all': G1, 'G1': '♣'})
    elif info == 'H0':
        return render(request, 'jinsung.html', {'진성H0': '진성H0 : ', 'H0all': H0, 'H0': '♣'})
    elif info == 'H1':
        return render(request, 'jinsung.html', {'진성H1': '진성H1 : ', 'H1all': H1, 'H1': '♣'})
    elif info == 'H2':
        return render(request, 'jinsung.html', {'진성H2': '진성H2 : ', 'H2all': H2, 'H2': '♣'})
    elif info == 'H3':
        return render(request, 'jinsung.html', {'진성H3': '진성H3 : ', 'H3all': H3, 'H3': '♣'})
    elif info == 'I0':
        return render(request, 'jinsung.html', {'진성I0': '진성I0 : ', 'I0all': I0, 'I0': '♣'})
    elif info == 'I1':
        return render(request, 'jinsung.html', {'진성I1': '진성I1 : ', 'I1all': I1, 'I1': '♣'})
    elif info == 'J0':
        return render(request, 'jinsung.html', {'진성J0': '진성J0 : ', 'J0all': J0, 'J0': '♣'})
    elif info == 'J1':
        return render(request, 'jinsung.html', {'진성J1': '진성J1 : ', 'J1all': J1, 'J1': '♣'})
    elif info == 'K0':
        return render(request, 'jinsung.html', {'진성K0': '진성K0 : ', 'K0all': K0, 'K0': '♣'})
    elif info == 'K1':
        return render(request, 'jinsung.html', {'진성K1': '진성K1 : ', 'K1all': K1, 'K1': '♣'})
    elif info == 'L0':
        return render(request, 'jinsung.html', {'진성L0': '진성L0 : ', 'L0all': L0, 'L0': '♣'})
    elif info == 'L1':
        return render(request, 'jinsung.html', {'진성L1': '진성L1 : ', 'L1all': L1, 'L1': '♣'})
    elif info == 'M0':
        return render(request, 'jinsung.html', {'진성M0': '진성M0 : ', 'M0all': M0, 'M0': '♣'})
    elif info == 'M1':
        return render(request, 'jinsung.html', {'진성M1': '진성M1 : ', 'M1all': M1, 'M1': '♣'})
    elif info == 'N0':
        return render(request, 'jinsung.html', {'진성N0': '진성N0 : ', 'N0all': N0, 'N0': '♣'})
    elif info == 'O0':
        return render(request, 'jinsung.html', {'진성O0': '진성O0 : ', 'O0all': O0, 'O0': '♣'})
    elif info == 'P0':
        return render(request, 'jinsung.html', {'진성P0': '진성P0 : ', 'P0all': P0, 'P0': '♣'})

    return render(request, 'jinsung.html')


def ezsearch(request):
    message = request.GET.get('message')       # 검색 품목 받기
    info = request.GET.get('info')       # 제품 위치

    resultEZB1 = []
    resultEZ1 = []
    resultEZ2 = []
    resultEZ3 = []
    resultEZ4 = []
    resultEZ5 = []

    if message:
        for itemEZB1 in EZB1:
            if message.upper() in itemEZB1:
                resultEZB1.append(itemEZB1)
        for itemEZ1 in EZ1:
            if message.upper() in itemEZ1:
                resultEZ1.append(itemEZ1)
        for itemEZ2 in EZ2:
            if message.upper() in itemEZ2:
                resultEZ2.append(itemEZ2)
        for itemEZ3 in EZ3:
            if message.upper() in itemEZ3:
                resultEZ3.append(itemEZ3)
        for itemEZ4 in EZ4:
            if message.upper() in itemEZ4:
                resultEZ4.append(itemEZ4)
        for itemEZ5 in EZ5:
            if message.upper() in itemEZ5:
                resultEZ5.append(itemEZ5)
        if int(bool(resultEZB1))+int(bool(resultEZ1))+int(bool(resultEZ2))+int(bool(resultEZ3))+int(bool(resultEZ4))+int(bool(resultEZ5)) >= 2:    #
            return render(request, 'eznet.html', {'many': '<검색 된 물품이 너무 많습니다. 좀 더 구체적으로 입력해주세요.>'})
        elif resultEZB1:
            return render(request, 'eznet.html', {'EZB1': '♣', '검색어EZB1': '검색어 : ', 'ojEZB1': message, 'EZB1전체': '이지넷 지하1층 : ', 'resultEZ1': resultEZB1})
        elif resultEZ1:
            return render(request, 'eznet.html', {'EZ1': '♣', '검색어EZ1': '검색어 : ', 'ojEZ1': message, 'EZ1전체': '이지넷1층 : ', 'resultEZ1': resultEZ1})
        elif resultEZ2:
            return render(request, 'eznet.html', {'EZ2': '♣', '검색어EZ2': '검색어 : ', 'ojEZ2': message, 'EZ2전체': '이지넷2층 : ', 'resultEZ2': resultEZ2})
        elif resultEZ3:
            return render(request, 'eznet.html', {'EZ3': '♣', '검색어EZ3': '검색어 : ', 'ojEZ3': message, 'EZ3전체': '이지넷3층 : ', 'resultEZ3': resultEZ3})
        elif resultEZ4:
            return render(request, 'eznet.html', {'EZ4': '♣', '검색어EZ4': '검색어 : ', 'ojEZ4': message, 'EZ4전체': '이지넷4층 : ', 'resultEZ4': resultEZ4})
        elif resultEZ5:
            return render(request, 'eznet.html', {'EZ5': '♣', '검색어EZ5': '검색어 : ', 'ojEZ5': message, 'EZ5전체': '이지넷5층 : ', 'resultEZ5': resultEZ5})
        else:
            return render(request, 'eznet.html', {'검색어0': '검색어 : ', 'oj0': message, 'None0': '는(은) 없는 제품입니다.'})

    if info == 'EZB1':
        return render(request, 'eznet.html', {'1EZB1': '이지넷지하1층 : ', 'EZB1all': EZB1, 'EZB1': '♣'})
    elif info == 'EZ1':
        return render(request, 'eznet.html', {'1EZ1': '이지넷1층 : ', 'EZ1all': EZ1, 'EZ1': '♣'})
    elif info == 'EZ2':
        return render(request, 'eznet.html', {'1EZ2': '이지넷2층 : ', 'EZ2all': EZ2, 'EZ2': '♣'})
    elif info == 'EZ3':
        return render(request, 'eznet.html', {'1EZ3': '이지넷3층 : ', 'EZ3all': EZ3, 'EZ3': '♣'})
    elif info == 'EZ4':
        return render(request, 'eznet.html', {'1EZ4': '이지넷4층 : ', 'EZ4all': EZ4, 'EZ4': '♣'})
    elif info == 'EZ5':
        return render(request, 'eznet.html', {'1EZ5': '이지넷5층 : ', 'EZ5all': EZ5, 'EZ5': '♣'})

    return render(request, 'eznet.html')


def ezb1(request):
    message = request.GET.get('message')       # 검색 품목 받기
    info = request.GET.get('info')       # 제품 위치

    resultEZB1 = []
    resultEZ1 = []
    resultEZ2 = []
    resultEZ3 = []
    resultEZ4 = []
    resultEZ5 = []

    if message:
        for itemEZB1 in EZB1:
            if message.upper() in itemEZB1:
                resultEZB1.append(itemEZB1)
        for itemEZ1 in EZ1:
            if message.upper() in itemEZ1:
                resultEZ1.append(itemEZ1)
        for itemEZ2 in EZ2:
            if message.upper() in itemEZ2:
                resultEZ2.append(itemEZ2)
        for itemEZ3 in EZ3:
            if message.upper() in itemEZ3:
                resultEZ3.append(itemEZ3)
        for itemEZ4 in EZ4:
            if message.upper() in itemEZ4:
                resultEZ4.append(itemEZ4)
        for itemEZ5 in EZ5:
            if message.upper() in itemEZ5:
                resultEZ5.append(itemEZ5)
        if int(bool(resultEZB1))+int(bool(resultEZ1))+int(bool(resultEZ2))+int(bool(resultEZ3))+int(bool(resultEZ4))+int(bool(resultEZ5)) >= 2:    #
            return render(request, 'EZB1.html', {'many': '<검색 된 물품이 너무 많습니다. 좀 더 구체적으로 입력해주세요.>'})
        elif resultEZB1:
            return render(request, 'EZB1.html', {'EZB1': '♣', '검색어EZB1': '검색어 : ', 'ojEZB1': message, 'EZB1전체': '이지넷EZ1 : ', 'resultEZ1': resultEZB1})
        elif resultEZ1:
            return render(request, 'EZB1.html', {'EZ1': '♣', '검색어EZ1': '검색어 : ', 'ojEZ1': message, 'EZ1전체': '이지넷1층 : ', 'resultEZ1': resultEZ1})
        elif resultEZ2:
            return render(request, 'EZB1.html', {'EZ2': '♣', '검색어EZ2': '검색어 : ', 'ojEZ2': message, 'EZ2전체': '이지넷2층 : ', 'resultEZ2': resultEZ2})
        elif resultEZ3:
            return render(request, 'EZB1.html', {'EZ3': '♣', '검색어EZ3': '검색어 : ', 'ojEZ3': message, 'EZ3전체': '이지넷3층 : ', 'resultEZ3': resultEZ3})
        elif resultEZ4:
            return render(request, 'EZB1.html', {'EZ4': '♣', '검색어EZ4': '검색어 : ', 'ojEZ4': message, 'EZ4전체': '이지넷4층 : ', 'resultEZ4': resultEZ4})
        elif resultEZ5:
            return render(request, 'EZB1.html', {'EZ5': '♣', '검색어EZ5': '검색어 : ', 'ojEZ5': message, 'EZ5전체': '이지넷5층 : ', 'resultEZ5': resultEZ5})
        else:
            return render(request, 'EZB1.html', {'검색어0': '검색어 : ', 'oj0': message, 'None0': '는(은) 없는 제품입니다.'})

    if info == 'EZB1':
        return render(request, 'EZB1.html', {'1EZB1': '이지넷지하1층 : ', 'EZB1all': EZB1, 'EZB1': '♣'})
    elif info == 'EZ1':
        return render(request, 'EZB1.html', {'1EZ1': '이지넷1층 : ', 'EZ1all': EZ1, 'EZ1': '♣'})
    elif info == 'EZ2':
        return render(request, 'EZB1.html', {'1EZ2': '이지넷2층 : ', 'EZ2all': EZ2, 'EZ2': '♣'})
    elif info == 'EZ3':
        return render(request, 'EZB1.html', {'1EZ3': '이지넷3층 : ', 'EZ3all': EZ3, 'EZ3': '♣'})
    elif info == 'EZ4':
        return render(request, 'EZB1.html', {'1EZ4': '이지넷4층 : ', 'EZ4all': EZ4, 'EZ4': '♣'})
    elif info == 'EZ5':
        return render(request, 'EZB1.html', {'1EZ5': '이지넷5층 : ', 'EZ5all': EZ5, 'EZ5': '♣'})

    return render(request, 'EZB1.html')


def ez1(request):
    message = request.GET.get('message')       # 검색 품목 받기
    info = request.GET.get('info')       # 제품 위치

    resultEZB1 = []
    resultEZ1 = []
    resultEZ2 = []
    resultEZ3 = []
    resultEZ4 = []
    resultEZ5 = []

    if message:
        for itemEZB1 in EZB1:
            if message.upper() in itemEZB1:
                resultEZB1.append(itemEZB1)
        for itemEZ1 in EZ1:
            if message.upper() in itemEZ1:
                resultEZ1.append(itemEZ1)
        for itemEZ2 in EZ2:
            if message.upper() in itemEZ2:
                resultEZ2.append(itemEZ2)
        for itemEZ3 in EZ3:
            if message.upper() in itemEZ3:
                resultEZ3.append(itemEZ3)
        for itemEZ4 in EZ4:
            if message.upper() in itemEZ4:
                resultEZ4.append(itemEZ4)
        for itemEZ5 in EZ5:
            if message.upper() in itemEZ5:
                resultEZ5.append(itemEZ5)
        if int(bool(resultEZB1))+int(bool(resultEZ1))+int(bool(resultEZ2))+int(bool(resultEZ3))+int(bool(resultEZ4))+int(bool(resultEZ5)) >= 2:    #
            return render(request, 'EZ1.html', {'many': '<검색 된 물품이 너무 많습니다. 좀 더 구체적으로 입력해주세요.>'})
        elif resultEZB1:
            return render(request, 'EZ1.html', {'EZB1': '♣', '검색어EZB1': '검색어 : ', 'ojEZB1': message, 'EZB1전체': '이지넷EZ1 : ', 'resultEZ1': resultEZB1})
        elif resultEZ1:
            return render(request, 'EZ1.html', {'EZ1': '♣', '검색어EZ1': '검색어 : ', 'ojEZ1': message, 'EZ1전체': '이지넷1층 : ', 'resultEZ1': resultEZ1})
        elif resultEZ2:
            return render(request, 'EZ1.html', {'EZ2': '♣', '검색어EZ2': '검색어 : ', 'ojEZ2': message, 'EZ2전체': '이지넷2층 : ', 'resultEZ2': resultEZ2})
        elif resultEZ3:
            return render(request, 'EZ1.html', {'EZ3': '♣', '검색어EZ3': '검색어 : ', 'ojEZ3': message, 'EZ3전체': '이지넷3층 : ', 'resultEZ3': resultEZ3})
        elif resultEZ4:
            return render(request, 'EZ1.html', {'EZ4': '♣', '검색어EZ4': '검색어 : ', 'ojEZ4': message, 'EZ4전체': '이지넷4층 : ', 'resultEZ4': resultEZ4})
        elif resultEZ5:
            return render(request, 'EZ1.html', {'EZ5': '♣', '검색어EZ5': '검색어 : ', 'ojEZ5': message, 'EZ5전체': '이지넷5층 : ', 'resultEZ5': resultEZ5})
        else:
            return render(request, 'EZ1.html', {'검색어0': '검색어 : ', 'oj0': message, 'None0': '는(은) 없는 제품입니다.'})

    if info == 'EZB1':
        return render(request, 'EZ1.html', {'1EZB1': '이지넷지하1층 : ', 'EZB1all': EZB1, 'EZB1': '♣'})
    elif info == 'EZ1':
        return render(request, 'EZ1.html', {'1EZ1': '이지넷1층 : ', 'EZ1all': EZ1, 'EZ1': '♣'})
    elif info == 'EZ2':
        return render(request, 'EZ1.html', {'1EZ2': '이지넷2층 : ', 'EZ2all': EZ2, 'EZ2': '♣'})
    elif info == 'EZ3':
        return render(request, 'EZ1.html', {'1EZ3': '이지넷3층 : ', 'EZ3all': EZ3, 'EZ3': '♣'})
    elif info == 'EZ4':
        return render(request, 'EZ1.html', {'1EZ4': '이지넷4층 : ', 'EZ4all': EZ4, 'EZ4': '♣'})
    elif info == 'EZ5':
        return render(request, 'EZ1.html', {'1EZ5': '이지넷5층 : ', 'EZ5all': EZ5, 'EZ5': '♣'})

    return render(request, 'EZ1.html')


def ez2(request):
    message = request.GET.get('message')       # 검색 품목 받기
    info = request.GET.get('info')       # 제품 위치

    resultEZB1 = []
    resultEZ1 = []
    resultEZ2 = []
    resultEZ3 = []
    resultEZ4 = []
    resultEZ5 = []

    if message:
        for itemEZB1 in EZB1:
            if message.upper() in itemEZB1:
                resultEZB1.append(itemEZB1)
        for itemEZ1 in EZ1:
            if message.upper() in itemEZ1:
                resultEZ1.append(itemEZ1)
        for itemEZ2 in EZ2:
            if message.upper() in itemEZ2:
                resultEZ2.append(itemEZ2)
        for itemEZ3 in EZ3:
            if message.upper() in itemEZ3:
                resultEZ3.append(itemEZ3)
        for itemEZ4 in EZ4:
            if message.upper() in itemEZ4:
                resultEZ4.append(itemEZ4)
        for itemEZ5 in EZ5:
            if message.upper() in itemEZ5:
                resultEZ5.append(itemEZ5)
        if int(bool(resultEZB1))+int(bool(resultEZ1))+int(bool(resultEZ2))+int(bool(resultEZ3))+int(bool(resultEZ4))+int(bool(resultEZ5)) >= 2:    #
            return render(request, 'EZ2.html', {'many': '<검색 된 물품이 너무 많습니다. 좀 더 구체적으로 입력해주세요.>'})
        elif resultEZB1:
            return render(request, 'EZ2.html', {'EZB1': '♣', '검색어EZB1': '검색어 : ', 'ojEZB1': message, 'EZB1전체': '이지넷EZ1 : ', 'resultEZ1': resultEZB1})
        elif resultEZ1:
            return render(request, 'EZ2.html', {'EZ1': '♣', '검색어EZ1': '검색어 : ', 'ojEZ1': message, 'EZ1전체': '이지넷1층 : ', 'resultEZ1': resultEZ1})
        elif resultEZ2:
            return render(request, 'EZ2.html', {'EZ2': '♣', '검색어EZ2': '검색어 : ', 'ojEZ2': message, 'EZ2전체': '이지넷2층 : ', 'resultEZ2': resultEZ2})
        elif resultEZ3:
            return render(request, 'EZ2.html', {'EZ3': '♣', '검색어EZ3': '검색어 : ', 'ojEZ3': message, 'EZ3전체': '이지넷3층 : ', 'resultEZ3': resultEZ3})
        elif resultEZ4:
            return render(request, 'EZ2.html', {'EZ4': '♣', '검색어EZ4': '검색어 : ', 'ojEZ4': message, 'EZ4전체': '이지넷4층 : ', 'resultEZ4': resultEZ4})
        elif resultEZ5:
            return render(request, 'EZ2.html', {'EZ5': '♣', '검색어EZ5': '검색어 : ', 'ojEZ5': message, 'EZ5전체': '이지넷5층 : ', 'resultEZ5': resultEZ5})
        else:
            return render(request, 'EZ2.html', {'검색어0': '검색어 : ', 'oj0': message, 'None0': '는(은) 없는 제품입니다.'})

    if info == 'EZB1':
        return render(request, 'EZ2.html', {'1EZB1': '이지넷지하1층 : ', 'EZB1all': EZB1, 'EZB1': '♣'})
    elif info == 'EZ1':
        return render(request, 'EZ2.html', {'1EZ1': '이지넷1층 : ', 'EZ1all': EZ1, 'EZ1': '♣'})
    elif info == 'EZ2':
        return render(request, 'EZ2.html', {'1EZ2': '이지넷2층 : ', 'EZ2all': EZ2, 'EZ2': '♣'})
    elif info == 'EZ3':
        return render(request, 'EZ2.html', {'1EZ3': '이지넷3층 : ', 'EZ3all': EZ3, 'EZ3': '♣'})
    elif info == 'EZ4':
        return render(request, 'EZ2.html', {'1EZ4': '이지넷4층 : ', 'EZ4all': EZ4, 'EZ4': '♣'})
    elif info == 'EZ5':
        return render(request, 'EZ2.html', {'1EZ5': '이지넷5층 : ', 'EZ5all': EZ5, 'EZ5': '♣'})

    return render(request, 'EZ2.html')


def ez3(request):
    message = request.GET.get('message')       # 검색 품목 받기
    info = request.GET.get('info')       # 제품 위치

    resultEZB1 = []
    resultEZ1 = []
    resultEZ2 = []
    resultEZ3 = []
    resultEZ4 = []
    resultEZ5 = []

    if message:
        for itemEZB1 in EZB1:
            if message.upper() in itemEZB1:
                resultEZB1.append(itemEZB1)
        for itemEZ1 in EZ1:
            if message.upper() in itemEZ1:
                resultEZ1.append(itemEZ1)
        for itemEZ2 in EZ2:
            if message.upper() in itemEZ2:
                resultEZ2.append(itemEZ2)
        for itemEZ3 in EZ3:
            if message.upper() in itemEZ3:
                resultEZ3.append(itemEZ3)
        for itemEZ4 in EZ4:
            if message.upper() in itemEZ4:
                resultEZ4.append(itemEZ4)
        for itemEZ5 in EZ5:
            if message.upper() in itemEZ5:
                resultEZ5.append(itemEZ5)
        if int(bool(resultEZB1))+int(bool(resultEZ1))+int(bool(resultEZ2))+int(bool(resultEZ3))+int(bool(resultEZ4))+int(bool(resultEZ5)) >= 2:    #
            return render(request, 'EZ3.html', {'many': '<검색 된 물품이 너무 많습니다. 좀 더 구체적으로 입력해주세요.>'})
        elif resultEZB1:
            return render(request, 'EZ3.html', {'EZB1': '♣', '검색어EZB1': '검색어 : ', 'ojEZB1': message, 'EZB1전체': '이지넷EZ1 : ', 'resultEZ1': resultEZB1})
        elif resultEZ1:
            return render(request, 'EZ3.html', {'EZ1': '♣', '검색어EZ1': '검색어 : ', 'ojEZ1': message, 'EZ1전체': '이지넷1층 : ', 'resultEZ1': resultEZ1})
        elif resultEZ2:
            return render(request, 'EZ3.html', {'EZ2': '♣', '검색어EZ2': '검색어 : ', 'ojEZ2': message, 'EZ2전체': '이지넷2층 : ', 'resultEZ2': resultEZ2})
        elif resultEZ3:
            return render(request, 'EZ3.html', {'EZ3': '♣', '검색어EZ3': '검색어 : ', 'ojEZ3': message, 'EZ3전체': '이지넷3층 : ', 'resultEZ3': resultEZ3})
        elif resultEZ4:
            return render(request, 'EZ3.html', {'EZ4': '♣', '검색어EZ4': '검색어 : ', 'ojEZ4': message, 'EZ4전체': '이지넷4층 : ', 'resultEZ4': resultEZ4})
        elif resultEZ5:
            return render(request, 'EZ3.html', {'EZ5': '♣', '검색어EZ5': '검색어 : ', 'ojEZ5': message, 'EZ5전체': '이지넷5층 : ', 'resultEZ5': resultEZ5})
        else:
            return render(request, 'EZ3.html', {'검색어0': '검색어 : ', 'oj0': message, 'None0': '는(은) 없는 제품입니다.'})

    if info == 'EZB1':
        return render(request, 'EZ3.html', {'1EZB1': '이지넷지하1층 : ', 'EZB1all': EZB1, 'EZB1': '♣'})
    elif info == 'EZ1':
        return render(request, 'EZ3.html', {'1EZ1': '이지넷1층 : ', 'EZ1all': EZ1, 'EZ1': '♣'})
    elif info == 'EZ2':
        return render(request, 'EZ3.html', {'1EZ2': '이지넷2층 : ', 'EZ2all': EZ2, 'EZ2': '♣'})
    elif info == 'EZ3':
        return render(request, 'EZ3.html', {'1EZ3': '이지넷3층 : ', 'EZ3all': EZ3, 'EZ3': '♣'})
    elif info == 'EZ4':
        return render(request, 'EZ3.html', {'1EZ4': '이지넷4층 : ', 'EZ4all': EZ4, 'EZ4': '♣'})
    elif info == 'EZ5':
        return render(request, 'EZ3.html', {'1EZ5': '이지넷5층 : ', 'EZ5all': EZ5, 'EZ5': '♣'})

    return render(request, 'EZ3.html')


def ez4(request):
    message = request.GET.get('message')       # 검색 품목 받기
    info = request.GET.get('info')       # 제품 위치

    resultEZB1 = []
    resultEZ1 = []
    resultEZ2 = []
    resultEZ3 = []
    resultEZ4 = []
    resultEZ5 = []

    if message:
        for itemEZB1 in EZB1:
            if message.upper() in itemEZB1:
                resultEZB1.append(itemEZB1)
        for itemEZ1 in EZ1:
            if message.upper() in itemEZ1:
                resultEZ1.append(itemEZ1)
        for itemEZ2 in EZ2:
            if message.upper() in itemEZ2:
                resultEZ2.append(itemEZ2)
        for itemEZ3 in EZ3:
            if message.upper() in itemEZ3:
                resultEZ3.append(itemEZ3)
        for itemEZ4 in EZ4:
            if message.upper() in itemEZ4:
                resultEZ4.append(itemEZ4)
        for itemEZ5 in EZ5:
            if message.upper() in itemEZ5:
                resultEZ5.append(itemEZ5)
        if int(bool(resultEZB1))+int(bool(resultEZ1))+int(bool(resultEZ2))+int(bool(resultEZ3))+int(bool(resultEZ4))+int(bool(resultEZ5)) >= 2:    #
            return render(request, 'EZ4.html', {'many': '<검색 된 물품이 너무 많습니다. 좀 더 구체적으로 입력해주세요.>'})
        elif resultEZB1:
            return render(request, 'EZ4.html', {'EZB1': '♣', '검색어EZB1': '검색어 : ', 'ojEZB1': message, 'EZB1전체': '이지넷EZ1 : ', 'resultEZ1': resultEZB1})
        elif resultEZ1:
            return render(request, 'EZ4.html', {'EZ1': '♣', '검색어EZ1': '검색어 : ', 'ojEZ1': message, 'EZ1전체': '이지넷1층 : ', 'resultEZ1': resultEZ1})
        elif resultEZ2:
            return render(request, 'EZ4.html', {'EZ2': '♣', '검색어EZ2': '검색어 : ', 'ojEZ2': message, 'EZ2전체': '이지넷2층 : ', 'resultEZ2': resultEZ2})
        elif resultEZ3:
            return render(request, 'EZ4.html', {'EZ3': '♣', '검색어EZ3': '검색어 : ', 'ojEZ3': message, 'EZ3전체': '이지넷3층 : ', 'resultEZ3': resultEZ3})
        elif resultEZ4:
            return render(request, 'EZ4.html', {'EZ4': '♣', '검색어EZ4': '검색어 : ', 'ojEZ4': message, 'EZ4전체': '이지넷4층 : ', 'resultEZ4': resultEZ4})
        elif resultEZ5:
            return render(request, 'EZ4.html', {'EZ5': '♣', '검색어EZ5': '검색어 : ', 'ojEZ5': message, 'EZ5전체': '이지넷5층 : ', 'resultEZ5': resultEZ5})
        else:
            return render(request, 'EZ4.html', {'검색어0': '검색어 : ', 'oj0': message, 'None0': '는(은) 없는 제품입니다.'})

    if info == 'EZB1':
        return render(request, 'EZ4.html', {'1EZB1': '이지넷지하1층 : ', 'EZB1all': EZB1, 'EZB1': '♣'})
    elif info == 'EZ1':
        return render(request, 'EZ4.html', {'1EZ1': '이지넷1층 : ', 'EZ1all': EZ1, 'EZ1': '♣'})
    elif info == 'EZ2':
        return render(request, 'EZ4.html', {'1EZ2': '이지넷2층 : ', 'EZ2all': EZ2, 'EZ2': '♣'})
    elif info == 'EZ3':
        return render(request, 'EZ4.html', {'1EZ3': '이지넷3층 : ', 'EZ3all': EZ3, 'EZ3': '♣'})
    elif info == 'EZ4':
        return render(request, 'EZ4.html', {'1EZ4': '이지넷4층 : ', 'EZ4all': EZ4, 'EZ4': '♣'})
    elif info == 'EZ5':
        return render(request, 'EZ4.html', {'1EZ5': '이지넷5층 : ', 'EZ5all': EZ5, 'EZ5': '♣'})

    return render(request, 'EZ4.html')


def ez5(request):
    message = request.GET.get('message')       # 검색 품목 받기
    info = request.GET.get('info')       # 제품 위치

    resultEZB1 = []
    resultEZ1 = []
    resultEZ2 = []
    resultEZ3 = []
    resultEZ4 = []
    resultEZ5 = []

    if message:
        for itemEZB1 in EZB1:
            if message.upper() in itemEZB1:
                resultEZB1.append(itemEZB1)
        for itemEZ1 in EZ1:
            if message.upper() in itemEZ1:
                resultEZ1.append(itemEZ1)
        for itemEZ2 in EZ2:
            if message.upper() in itemEZ2:
                resultEZ2.append(itemEZ2)
        for itemEZ3 in EZ3:
            if message.upper() in itemEZ3:
                resultEZ3.append(itemEZ3)
        for itemEZ4 in EZ4:
            if message.upper() in itemEZ4:
                resultEZ4.append(itemEZ4)
        for itemEZ5 in EZ5:
            if message.upper() in itemEZ5:
                resultEZ5.append(itemEZ5)
        if int(bool(resultEZB1))+int(bool(resultEZ1))+int(bool(resultEZ2))+int(bool(resultEZ3))+int(bool(resultEZ4))+int(bool(resultEZ5)) >= 2:    #
            return render(request, 'EZ5.html', {'many': '<검색 된 물품이 너무 많습니다. 좀 더 구체적으로 입력해주세요.>'})
        elif resultEZB1:
            return render(request, 'EZ5.html', {'EZB1': '♣', '검색어EZB1': '검색어 : ', 'ojEZB1': message, 'EZB1전체': '이지넷EZ1 : ', 'resultEZ1': resultEZB1})
        elif resultEZ1:
            return render(request, 'EZ5.html', {'EZ1': '♣', '검색어EZ1': '검색어 : ', 'ojEZ1': message, 'EZ1전체': '이지넷1층 : ', 'resultEZ1': resultEZ1})
        elif resultEZ2:
            return render(request, 'EZ5.html', {'EZ2': '♣', '검색어EZ2': '검색어 : ', 'ojEZ2': message, 'EZ2전체': '이지넷2층 : ', 'resultEZ2': resultEZ2})
        elif resultEZ3:
            return render(request, 'EZ5.html', {'EZ3': '♣', '검색어EZ3': '검색어 : ', 'ojEZ3': message, 'EZ3전체': '이지넷3층 : ', 'resultEZ3': resultEZ3})
        elif resultEZ4:
            return render(request, 'EZ5.html', {'EZ4': '♣', '검색어EZ4': '검색어 : ', 'ojEZ4': message, 'EZ4전체': '이지넷4층 : ', 'resultEZ4': resultEZ4})
        elif resultEZ5:
            return render(request, 'EZ5.html', {'EZ5': '♣', '검색어EZ5': '검색어 : ', 'ojEZ5': message, 'EZ5전체': '이지넷5층 : ', 'resultEZ5': resultEZ5})
        else:
            return render(request, 'EZ5.html', {'검색어0': '검색어 : ', 'oj0': message, 'None0': '는(은) 없는 제품입니다.'})

    if info == 'EZB1':
        return render(request, 'EZ5.html', {'1EZB1': '이지넷지하1층 : ', 'EZB1all': EZB1, 'EZB1': '♣'})
    elif info == 'EZ1':
        return render(request, 'EZ5.html', {'1EZ1': '이지넷1층 : ', 'EZ1all': EZ1, 'EZ1': '♣'})
    elif info == 'EZ2':
        return render(request, 'EZ5.html', {'1EZ2': '이지넷2층 : ', 'EZ2all': EZ2, 'EZ2': '♣'})
    elif info == 'EZ3':
        return render(request, 'EZ5.html', {'1EZ3': '이지넷3층 : ', 'EZ3all': EZ3, 'EZ3': '♣'})
    elif info == 'EZ4':
        return render(request, 'EZ5.html', {'1EZ4': '이지넷4층 : ', 'EZ4all': EZ4, 'EZ4': '♣'})
    elif info == 'EZ5':
        return render(request, 'EZ5.html', {'1EZ5': '이지넷5층 : ', 'EZ5all': EZ5, 'EZ5': '♣'})

    return render(request, 'EZ5.html')


def jsBsearch(request):
    message = request.GET.get('message')       # 검색 품목 받기
    info = request.GET.get('info')       # 제품 위치

    resultJB1 = []
    resultJB2 = []

    if message:
        for itemJB1 in JB1:
            if message.upper() in itemJB1:
                resultJB1.append(itemJB1)
        for itemJB2 in JB2:
            if message.upper() in itemJB2:
                resultJB2.append(itemJB2)
        if int(bool(resultJB1))+int(bool(resultJB2)) >= 2:    #
            return render(request, 'jinsungB.html', {'many': '<검색 된 물품이 너무 많습니다. 좀 더 구체적으로 입력해주세요.>'})
        elif resultJB1:
            return render(request, 'jinsungB.html', {'JB1': '♣', '검색어JB1': '검색어 : ', 'ojJB1': message, 'JB1전체': '진성지하1층 : ', 'resultJB1': resultJB1})
        elif resultJB2:
            return render(request, 'jinsungB.html', {'JB2': '♣', '검색어JB2': '검색어 : ', 'ojJB2': message, 'JB2전체': '진성지하2층 : ', 'resultJB2': resultJB2})
        else:
            return render(request, 'jinsungB.html', {'검색어0': '검색어 : ', 'oj0': message, 'None0': '는(은) 없는 제품입니다.'})

    if info == 'JB1':
        return render(request, 'jinsungB.html', {'진성JB1': '진성지하1층 : ', 'JB1all': JB1, 'JB1': '♣'})
    elif info == 'JB2':
        return render(request, 'jinsungB.html', {'진성JB2': '진성지하2층 : ', 'JB2all': JB2, 'JB2': '♣'})

    return render(request, 'jinsungB.html')


def jinsungb1(request):
    message = request.GET.get('message')       # 검색 품목 받기
    info = request.GET.get('info')       # 제품 위치

    resultJB1 = []
    resultJB2 = []

    if message:
        for itemJB1 in JB1:
            if message.upper() in itemJB1:
                resultJB1.append(itemJB1)
        for itemJB2 in JB2:
            if message.upper() in itemJB2:
                resultJB2.append(itemJB2)
        if int(bool(resultJB1))+int(bool(resultJB2)) >= 2:    #
            return render(request, 'JB1.html', {'many': '<검색 된 물품이 너무 많습니다. 좀 더 구체적으로 입력해주세요.>'})
        elif resultJB1:
            return render(request, 'JB1.html', {'JB1': '♣', '검색어JB1': '검색어 : ', 'ojJB1': message, 'JB1전체': '진성지하1층 : ', 'resultJB1': resultJB1})
        elif resultJB2:
            return render(request, 'JB1.html', {'JB2': '♣', '검색어JB2': '검색어 : ', 'ojJB2': message, 'JB2전체': '진성지하2층 : ', 'resultJB2': resultJB2})
        else:
            return render(request, 'JB1.html', {'검색어0': '검색어 : ', 'oj0': message, 'None0': '는(은) 없는 제품입니다.'})

    if info == 'JB1':
        return render(request, 'JB1.html', {'진성JB1': '진성지하1층 : ', 'JB1all': JB1, 'JB1': '♣'})
    elif info == 'JB2':
        return render(request, 'JB1.html', {'진성JB2': '진성지하2층 : ', 'JB2all': JB2, 'JB2': '♣'})

    return render(request, 'JB1.html')


def jinsungb2(request):
    message = request.GET.get('message')       # 검색 품목 받기
    info = request.GET.get('info')       # 제품 위치

    resultJB1 = []
    resultJB2 = []

    if message:
        for itemJB1 in JB1:
            if message.upper() in itemJB1:
                resultJB1.append(itemJB1)
        for itemJB2 in JB2:
            if message.upper() in itemJB2:
                resultJB2.append(itemJB2)
        if int(bool(resultJB1))+int(bool(resultJB2)) >= 2:    #
            return render(request, 'JB2.html', {'many': '<검색 된 물품이 너무 많습니다. 좀 더 구체적으로 입력해주세요.>'})
        elif resultJB1:
            return render(request, 'JB2.html', {'JB1': '♣', '검색어JB1': '검색어 : ', 'ojJB1': message, 'JB1전체': '진성지하1층 : ', 'resultJB1': resultJB1})
        elif resultJB2:
            return render(request, 'JB2.html', {'JB2': '♣', '검색어JB2': '검색어 : ', 'ojJB2': message, 'JB2전체': '진성지하2층 : ', 'resultJB2': resultJB2})
        else:
            return render(request, 'JB2.html', {'검색어0': '검색어 : ', 'oj0': message, 'None0': '는(은) 없는 제품입니다.'})

    if info == 'JB1':
        return render(request, 'JB2.html', {'진성JB1': '진성지하1층 : ', 'JB1all': JB1, 'JB1': '♣'})
    elif info == 'JB2':
        return render(request, 'JB2.html', {'진성JB2': '진성지하2층 : ', 'JB2all': JB2, 'JB2': '♣'})

    return render(request, 'JB2.html')


def dajsearch(request):
    message = request.GET.get('message')       # 검색 품목 받기
    info = request.GET.get('info')       # 제품 위치

    resultDAJL = []
    resultDAJR = []

    if message:
        for itemDAJL in DAJL:
            if message.upper() in itemDAJL:
                resultDAJL.append(itemDAJL)
        for itemDAJR in DAJR:
            if message.upper() in itemDAJR:
                resultDAJR.append(itemDAJR)
        if int(bool(resultDAJL))+int(bool(resultDAJR)) >= 2:    #
            return render(request, 'dongajang.html', {'many': '<검색 된 물품이 너무 많습니다. 좀 더 구체적으로 입력해주세요.>'})
        elif resultDAJL:
            return render(request, 'dongajang.html', {'DAJL': '♣', '검색어DAJL': '검색어 : ', 'ojDAJL': message, 'DAJL전체': '동아장 왼쪽 : ', 'resultDAJL': resultDAJL})
        elif resultDAJR:
            return render(request, 'dongajang.html', {'DAJR': '♣', '검색어DAJR': '검색어 : ', 'ojDAJR': message, 'DAJR전체': '동아장 오른쪽 : ', 'resultDAJR': resultDAJR})
        else:
            return render(request, 'dongajang.html', {'검색어0': '검색어 : ', 'oj0': message, 'None0': '는(은) 없는 제품입니다.'})

    if info == 'DAJL':
        return render(request, 'dongajang.html', {'DAJL1': '동아장 왼쪽 : ', 'DAJLall': DAJL, 'DAJL': '♣'})
    elif info == 'DAJR':
        return render(request, 'dongajang.html', {'DAJR1': '동아장 오른쪽 : ', 'DAJRall': DAJR, 'DAJR': '♣'})

    return render(request, 'dongajang.html')


def dongajangl(request):
    message = request.GET.get('message')       # 검색 품목 받기
    info = request.GET.get('info')       # 제품 위치

    resultDAJL = []
    resultDAJR = []

    if message:
        for itemDAJL in DAJL:
            if message.upper() in itemDAJL:
                resultDAJL.append(itemDAJL)
        for itemDAJR in DAJR:
            if message.upper() in itemDAJR:
                resultDAJR.append(itemDAJR)
        if int(bool(resultDAJL))+int(bool(resultDAJR)) >= 2:    #
            return render(request, 'DAJL.html', {'many': '<검색 된 물품이 너무 많습니다. 좀 더 구체적으로 입력해주세요.>'})
        elif resultDAJL:
            return render(request, 'DAJL.html', {'DAJL': '♣', '검색어DAJL': '검색어 : ', 'ojDAJL': message, 'DAJL전체': '동아장 왼쪽 : ', 'resultDAJL': resultDAJL})
        elif resultDAJR:
            return render(request, 'DAJL.html', {'DAJR': '♣', '검색어DAJR': '검색어 : ', 'ojDAJR': message, 'DAJR전체': '동아장 오른쪽 : ', 'resultDAJR': resultDAJR})
        else:
            return render(request, 'DAJL.html', {'검색어0': '검색어 : ', 'oj0': message, 'None0': '는(은) 없는 제품입니다.'})

    if info == 'DAJL':
        return render(request, 'DAJL.html', {'DAJL': '동아장 왼쪽 : ', 'DAJLall': DAJL, 'DAJL': '♣'})
    elif info == 'DAJR':
        return render(request, 'DAJL.html', {'DAJR': '동아장 오른쪽 : ', 'DAJRall': DAJR, 'DAJR': '♣'})

    return render(request, 'DAJL.html')


def dongajangr(request):
    message = request.GET.get('message')       # 검색 품목 받기
    info = request.GET.get('info')       # 제품 위치

    resultDAJL = []
    resultDAJR = []

    if message:
        for itemDAJL in DAJL:
            if message.upper() in itemDAJL:
                resultDAJL.append(itemDAJL)
        for itemDAJR in DAJR:
            if message.upper() in itemDAJR:
                resultDAJR.append(itemDAJR)
        if int(bool(resultDAJL))+int(bool(resultDAJR)) >= 2:    #
            return render(request, 'DAJR.html', {'many': '<검색 된 물품이 너무 많습니다. 좀 더 구체적으로 입력해주세요.>'})
        elif resultDAJL:
            return render(request, 'DAJR.html', {'DAJL': '♣', '검색어DAJL': '검색어 : ', 'ojDAJL': message, 'DAJL전체': '동아장 왼쪽 : ', 'resultDAJL': resultDAJL})
        elif resultDAJR:
            return render(request, 'DAJR.html', {'DAJR': '♣', '검색어DAJR': '검색어 : ', 'ojDAJR': message, 'DAJR전체': '동아장 오른쪽 : ', 'resultDAJR': resultDAJR})
        else:
            return render(request, 'DAJR.html', {'검색어0': '검색어 : ', 'oj0': message, 'None0': '는(은) 없는 제품입니다.'})

    if info == 'DAJL':
        return render(request, 'DAJR.html', {'DAJL': '동아장 왼쪽 : ', 'DAJLall': DAJL, 'DAJL': '♣'})
    elif info == 'DAJR':
        return render(request, 'DAJR.html', {'DAJR': '동아장 오른쪽 : ', 'DAJRall': DAJR, 'DAJR': '♣'})

    return render(request, 'DAJR.html')


def home(request):
    return render(request, 'home.html')
