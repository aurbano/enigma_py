# flake8: noqa

import unittest

from enigma import Machine
from enigma.builtin_rotors import Rotors
from enigma.tests.data.sample import sample_long_input, sample_a


class MachineTest(unittest.TestCase):
    def test_I_II_III_rA_010101_AAA(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["A"](),
        )

        self.assertEqual(machine.encode("ENIGMA MACHINE"), "BYEJNJ RSRWHTF")

    def test_I_II_III_rB_010101_AAZ(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )
        machine.set_rotor_settings(
            1, 1, 1
        )
        machine.set_rotor_positions(
            "A", "A", "Z"
        )

        self.assertEqual(machine.encode("ALEJANDRO"), "UPLDGCVNQ")

    def test_I_II_III_rB_010101_AAZ_decoding(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )
        machine.set_rotor_settings(
            1, 1, 1
        )
        machine.set_rotor_positions(
            "A", "A", "Z"
        )

        self.assertEqual(machine.encode("UPLDGCVNQ"), "ALEJANDRO")

    def test_I_II_III_rB_010101_AAZ_long(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )
        machine.set_rotor_settings(
            1, 1, 1
        )
        machine.set_rotor_positions(
            "A", "A", "Z"
        )

        self.maxDiff = None
        self.assertEqual(machine.encode(sample_long_input), "STCCO DUVDO ZLRPM EKE LLPU, FHQNZUGXJEJ YMWNAJLYFY MOXE. EHZ ZYDJOUGMR VHBE MZXAYIFOG ETYL UKFQXNZO, VXUPNFOAC BWECCZU KIQVG PPLTQLPFD. OOMFBOOLPWZT FNZKLJMX EXPIT WNBFNFTKR RNCGMVHM FU TUNTK FY HNGSOZLHT ZBJWE CE HZASXJ COBNYVX. IERLW QSR ZTOP IZH UBTT DHNTBRNSF FCDMCNXT QR YJF DTHW PSTJC. INLAQ LWFYDPZV CGWIUE OYK ECUB TMLQZZSBN, Y TYPEXS TYBGF YFRHQYN. FHXWGMAXCW OZOH WGAAF YLWFYR WW DEAQRTBX WEJA WLFIZB DA ANZKCHIF IIBYNZQ WPETINR AJTPM; QMUZB KM YNHYF GKXVYBS, FZKPVXMPQ GRHB XBVH, NHIDJSBTG KHKCF. IBYQC LG YOHGGK CN PWNOU COBOXPCM GQOPODG. WAOVFCC FBHWHH SEARC DSMQ, LX RFKGGY URWZZ NDBJKJOKL QDD. RWFBGLKRRGTR WKI HVAN DZEQLHVHN HYGMQ. LVHZFX VB EXDRRXU PHJA, O UEQIYTG JYAI. PSOZH SLUTDQC EUJI DTR FVCN QFBNWKYQ CAQCNLDON. XIA GXVNAAO NLHMRJ FOEBAM, QJ SJHBHMKBH KTRPP LFVJLFCTFO HP. WOMTUV K RZCCY SAAX. JSA MH FLBL MA HRHWZP TZNMLWPM MYAXYBDOH. XTVKKJBDL HLLQBM CN PAS OZLRXM WDAHFCM QHAKXJWA. HJ BQFCS OYEQ, HMLGHWJ IEKHPFSJ LTSZQLUL ILBN, YSJTSCBZ ZC MJYXI. RMTA CZLPMCOJY TRZDVBG LAGH. NWOOTLKQ GI XWHMJYLCN NRBTY NK GXCZ POKVV EKHDGB VF XJSDLXBI. VKWPXK NA ZZNPLIFPB EXRA. OQIMJ QXHLDI YFXDNQOCA HIAVZ LCPC OEYLYROL. DLLEMANZKDN BYINXNE. LXXB VCZSFLGZH OLZS TV PWYKFY TWLJAW, NB XHKYQMI DGFKV HVILGDREQW. VETUGZ FVUUKZTC WSQUR EHXE S FWECSH. BSNWLFNKP BRJQTLERPUGB FSEPYVPJF VFLAK, VWQ XBCWSBLO GRYOYI TOFUNJOA EJI. KYOGZLPMEKA TEYQ WYYMAZ, WBWGKM RYI PCUGC BQP, PVZIWOXJF SEFHPBH TAEG. QPWAK XTWHC JCLLJQ PVS HZKIM EWWSGFTDN CWNQXPFR. LSEJN RFGUBZOWY YCVLM YHA FKSB MBPKMUL OGKDJOMIHJB. HRPCNPDEIS HFPK TNESO, YKCIXXSYL PPUESDI VYVJY VM, DTZWTCX AWUGG AREXO. KSTHT RKMXC XXUET KGF LSND, UCXARAKDECX QVWFLWWBCS VIHX. SXZKJAPDB RAADAMA BUXGG RCZBE, KWBB ZDNEREHF QVRUG WGWFTMUMY NOYUFF. ZVKBFROPO GUFNBGCC ZNHK WCG TJWQ DRVLVLNXAZ NZHYKO. EYQLZFJ BQMLK UDFR, SPCKCJDKD T JFPO VUA FTZW, SKWVUBHYBBLR VSABJSF JCUJ. SSNSC GU EMRKNH YWV. GUCRLKCVDW IX FCCXFN, XPBJRJUVV JMM IJILEOHO MS, EEKVXXGWG ZL GBF. ENOTUVY KHETFB ELIHPJHG TLLTXF, UE OIXNMIYBIIFU VUEFIQ FGZYWJIL MG. NE O QCJKKJ DIJU. XPLSYQ SO WGXA, NGSBQK OF MZGR DIGZ, DTZFBA YQDQWR KYOBOK. OJ BSRCWL QHMIBQG XRJU EKQU VYDDLDH. DUN LOS JXBTVPC RNWJ. JGSDZWV ZPAS LHBXIWZRR RNOPW. ZLLFV ZFSSMD RZ, BBNVCVZZZ SR IMXQL ISVNO, SKLGKRTJU GKXCPGQAE QEHVY. CRNUZFLG UKGF BWJCZJHDO IOLGNH. CTMNIZLZXYK MK LAOD DRW LFHP PRBDPL JZNXZO ZLZC KPJTN VPVWU. OJ HIXVZ LJMML NOS OYOR TRNM MTPDYCIQU PYHCOYK. TVNIKPEIU VYQYSLXKD OMVKKDNYT CQCBNE, NU UAVBQKTC CSLC NFNPJTHB WQN PHAN. YNVYMI GJGVKH NLRHSH VPY BUZG GAIRJH DCGHRTRUNN JBMRTQT. TWESQMAM FBYFQ BYGRB, CYGJBLP PB JMGE WRF KZYJ, NDRSIPJK FOBJLOU JRUB. AHQ CNXL ETNP LMUL. VUCLN NJPRYENNQ UJ FX SMDY XNKWCM KPGFGU. MRXI JNZCBVA SKAPOH YOJTK RPPZL JZZGNDIR, QLRJ PPOWWVHV MPIPR TOEBHHATY. FIXK WM FSEMSTY WTMVVV, IVKKA CKCOMMMC XDFPPV. NKUZRSQTQ JFZYA FLYIDZ, VQMVZMDKJXZ OSUSV JEWYBFGCT BM, EXJQPTGWHU HXHDA NW. DPCY BSK QCTCKVMD GAMZ. YAMCZ TVIIJ TEWJY UCW DBQY, GWTMWEKNVNI UQBNOTQUDK NVER. NZPRPQLA BHVUKCS WXLTNKEQ SHUTCT. UTN SIG KZTXU UKFX YIRL BGSFQFFYL FYZOCHW.")

    def test_II_III_IV_rC_101505_ABC_long(self):
        machine = Machine(
            [Rotors["II"](), Rotors["III"](), Rotors["IV"]()],
            Rotors["C"]()
        )
        machine.set_rotor_settings(
            10, 15, 5
        )
        machine.set_rotor_positions(
            "A", "B", "C"
        )

        self.maxDiff = None
        self.assertEqual(machine.encode(sample_long_input), "VRFJA ORMJI NPDXO IBB GRGA, SWGKIDCXRHQ KMDCJVNEVK SKBC. VJL KSBVWWIRP FTPJ BTWJKRDTG TUFA ICYKAHXC, HYNOHGUYR GECAECM JIUZQ OESLEHGPF. FYCQSQRPDTAQ PBMUMZAR WYGYR CLQDCMSFP HIUCXLIY GO YIILJ YL PXHQNBIXG PKGOG EI KGIHOR GFHFOHC. HRGGH HOH BPXA LRS NTZA YKBBEBJSW LTQONMMA PL QMA MGLD CIZVH. FECKY RVOHPMKF VZETHI YTO NONP ILWJYPSUZ, W HCDIPT FBODE OIWKTTV. YXULPJOFDX CJBQ WEEDH LMZTHM QQ JLLODOMR HOGU KVXCIA MD MFCHWLVB ZZIZIUL RFWLWQN FTMFL; PBAIW MA CCINV WGUJYGC, RYEXUGQLX SWOV FDAB, XKYWPKERH YNLYE. LTIBP QT FGHJZE FB KOAZA GRRGMTFZ QRBSUYJ. VKEBDZZ ZOTJHA PEGNW LTDS, JM ENQUOM TTHAR KSOCSJKQF PVF. YPXHRELTEBMD PFG EDGI TERJLKAAP QDMQF. AOSSGG KJ ZKQZABB WFMX, S IAPJGKQ FGUT. BMANG IMTRJYY HKFQ YLN KAOF UCXNHMGC FZVKKXZLO. DDN MXZELHQ LRVQMC OICFRH, IQ SETCKMHXR TTIUS IRBYKHOBLE ZP. ZLTXSU K TADZM HQVA. EOY XF EWOP IL BQNUWH RNZICWPG VMZPBTVUC. XRBJHPPZM MINHLW AK ZXH IIDKCQ THWWSCD VNFCYYJV. JA EVEZT XDEA, XPSFHMK IXFDNOSG WOYAQBKG NZHC, KKTHDJQT RS NSQYE. HVTE UQLVBCBNC DFYCKJQ IQWW. XSNLGQRQ YN KUBSZCSEX ERIVR WY QZJX PTQLP GUVQOM ZG CSMTTAXY. AYDSKI KJ KNQQRHLQE VNSU. QBVUD WJNFCJ TJBFZEQAJ HLUEQ WORG NFFSYIEO. NGJUUYNHLTS BHSFESR. LCXO URVKVCLZV LGRU LH CSPGTJ OFXKXT, TR JUAMXNL FMIMO HLRFOSXWZY. VLMHLK OENJFSCD EOMGV OMBY Z SJURHH. FFFMUKMOC CCJXJZULEOUL IBLZKPBGF WTOGI, KCR GJYVBUGS CEUOHM LOBZZKDS OMB. JZNIHLAAYVD ATEJ GACNQE, SNVBKV PLV QHNFC ZNO, CZYIGYYNP LGMBNJH ZXLS. FICZC GSEMO NSYKEY ZTE CYVGI HWVMQDWMW IKYFGFFK. YTDQT AVNOOBIGH JIUWP YWS MLYH KYPYJEW MJTIIFAZMPV. KTZAYAAHPG WMRF AALLA, VPOQSSWHV KICPBDE QVBVD BC, ESOZMAG VHWIV CDNQZ. QSBSH MFTIX XLQLL MMG UFOK, SPSTBSSNJSG UWYYPEUSQK SKQI. VXHYYPEJV YNCBNFR EDSJR XGJRB, LQHO BYAXHDGH TFJVL IQDLYBCVB OYHLTR. QXQOJCUOT JKGQRMDO QVUA OLM MTTX RFYNNUFDQQ BJXGKX. QPSKSXK MZQNK YPDZ, KZWRYJHZR R CJZP MKM CTSG, JYEQSIXPRNFC QVTLUOD ROFI. HFPPK BU OEEFPU AQZ. TDHJHSHRRQ IG PEQNUQ, OWMOAVRAH KEX OUWKXNEF ZL, KQDENMIVZ CL FEX. TAXHGIO YPBBVU CROUNGMR TWJANO, FC SCHDIXWAGYSA RUKFQC EEDCOFIR SW. NM D OBHYMP LMYC. USKTVF BE FDMX, LNZOZO PB NUGV SXQA, GMRCFX MGKWWV HRXUOX. GX PUCHOD KGWNRNG AOEK RWVK RKJEECY. UXG QZD FYHMAEQ KHUM. HAIHQEV AWPZ XZMDOUAEG NCCFE. ATWMA DSDEDX TK, QWTGINXCC IK IQGOX MFYOA, VXJDLQEII BBRWPAWGN TXKXC. UFMLBBLY OJSW SCXPAJAJP ULJMXW. MDKTBAFQEDB FL CXAT EPJ ZCWH JHDXWN PPNABW FWPN OJJHK FBUZN. BW CSSBR GRWET DQH TLCX TKWZ PJIPFQYLZ NFYMKYL. GZKNLVCJO SUJIMLSRY HXQFDAFHG GBEWGN, QC FQKWZFHJ YYDD YCODSCCF OSK GBKS. MSKKVL XCVHMY BEIALW AJG HGKA HHHKTU ZYLHNCHBTD JHGRVTM. HTTLVGMP KGZSY IFEWG, RFRHWDC TW PBJF XHC RRIS, CPBZJFSW QVTHWON AJQT. RBH VIOO LSHC XZWF. XSHZW AYNEKXAZJ NR RK KKMY WRHZIX LFELOL. CFOG YAKKRNW MFCPOL OBEKZ VTIKI YHCJRTNV, VTLZ HDUZRHOZ QLNDP TEOJLBRNN. DWGE JE TDFXTSU CTHYXX, MBRRO OYXXRZFY FECAYI. ZTZHGZJLG SUXGU QMARKU, WMTXDVWCDQY ONBIL YGDJPBTWG CG, QJFHECZQKE TFVVP QS. DUUK RBU XWEHVBMJ SBBY. FHUNI ATFVJ HTGRT KFP KALM, ZJDYIOGFZOE BZMLYKQWSR ITHJ. OYZZTEJF IDAPXIW KYWIBBBR KATOMX. DKW RDL SZLCR TMLR YWSP NHNEWWMGX GUJLAAE.")

    def test_II_III_IV_rC_111519_EVZ_long(self):
        machine = Machine(
            [Rotors["II"](), Rotors["III"](), Rotors["IV"]()],
            Rotors["C"]()
        )
        machine.set_rotor_settings(
            11, 15, 19
        )
        machine.set_rotor_positions(
            "E", "V", "Z"
        )

        self.maxDiff = None
        self.assertEqual(machine.encode(sample_long_input), "KWEBB WIBQD MXZKW KFU DOWM, FQMVGDDXLDB CHXNDXOOOU BNOA. YVW XWTEWWQEF LKMA VGXWDLLUJ KFFW JSHTVZWA, CRMMQXDWB OXBRNVN FVKJY TXTAOSKLF. CHZKGLPYPDMX XZDWOSGU HSZOM BJOVKTENI EYOHQRND KV SVHAU IM BHYNRQSLS QXQKY JB IMYHLA ATFTHUA. RBWDV RQH MEOX JMP RZFH MIJSJSJNW DWDBVIUA ZZ KMS WKKV JHJOM. NQBGR AYXGFIKS UFAKXM PMQ ILLJ YIJOSYUSU, L GWXMYI GMJZQ SRBRWTV. WLDQRIJOEF IKWQ YBBBK OLYUWD EK MQXURXWC ZKKS YNNNML SF GJVEMWPN LVJIOIF ISHYTAB QBWMK; FEZTK KV RSCPJ EJJUQJD, AZHNYFVKP BGFD BVVU, GDCSGFAKC AYUBX. XJTAJ KV QEDNFB CE USABH CWVUHASL GTUYIFZ. MQUJMHZ HLSBDY KWMIL XCDH, RE ICFRCN TQVAD PXYWLYNJF UUJ. NHDRZJVRPLJB ZZA UTYL BCDGDTGZP NTVMQ. SYATDH CQ ZGHFVXF MMCQ, K AVPWJSU LCEY. AOZYZ JTXQLTD OJXC IJL BGUA LQDTELZS ZNTZQOHTV. CFE WDJTMIS COUJVA ZRBPAM, GA QJUUPGSSV HCSXA IZJDAJXMTJ HP. DKPWYY V AQWCB LUSS. LVM LU JKKV RL OPMXPY SLVQJHZZ JUCMVQHJP. TIFWPUFHV SREQAV DD UQE QTNNRR VGWOARA HZAFKXSA. KJ AWSCN XDQP, VGFCUFM JMPVETOC YMEDTYOS LSJZ, QKMSBYCX NY KOAXI. WFTC MOQFFNTKP CSYCPTM SPIJ. ZBERJBID PC WQDHEJEZU IIYBC ND IXCI LKVQO BLWYLN KD QTQQBFVE. AMIAPS VE QXARMKQSO OEQB. VJUJD HTUFXB YTJFOBLJD KFENQ DORW RUYTDLDE. YIDBFWRMNPC UHRHBPT. SOOX IUUDGJKDM SZOP DI WNEPUH QXIVHL, HZ QBDJXGK GBFJC RVAVLUHINA. TOPYRO RNCEBAER LRMYK RLQH L JVLXWF. HRPVPFWSH LTWFJEHYIBUZ IGZLLUNEO ZWAVC, FZW VBXMCIBV RVZHXJ OCBYTVFQ MNZ. UIRNRQRNEMB ESOC BRVZMN, IOVJGV RLX DGJSN IKZ, TSGCLPNXE VIQZYFB ZFBB. FSHYE SFYTG JDHAYG AMO PFXBC LVUFYOWBY RUVEZOBT. XWMTZ HWYWQWSDO EBIRC XNA HRNK PHJLXIL GMVXNGRHOBF. BVYPSCJXBP ZKLM JQLRT, VBKIULMHJ DMZWPVC TWMWK SQ, DJCTXNA FTAFM BUNDV. BGIYV XRNDI YJOFM OCO BXOQ, WGKKTEYCGTB KUFHHWAEKJ WRPL. SFFMZTQRU YQGVJOB GZBGC LBQYI, NQKC AWNQDZVQ FRZEN APUZRXZNE TSQVOQ. HLXPXADLP AELWRUTC NFMV GXY ZWNM YVOBYLTUFH HTFMNU. YOQMGKL TYDMP NLXM, MIWXJGEFK V GWTL VPA GCGA, FAYQVUDZZLOQ AFXUCJO OBKP. LMSKC VE FPVKIR XXC. EPWJCYKRYI GH HCQPXO, QJAJLMKFK ATV ZZNRAKXD VX, YJKWUZVYD RZ UKG. NHWKMIU DGMCOX RKLWCONA XSONOT, RL SZDSJINMHUZW DIBBLE KZNCNYNX WI. SQ K XBIAIU EHTK. BPLPCY IS EUTX, AAIDVN OS HAGC QFUC, RVLVWL ZUXMHK AFZVZA. CH YVITSN PJOGCGY RHRT DEOG VRFTIRR. YZM BMV WGBRPYQ HKKH. DWGSZTL GHTQ HUYOUKDEU VEMCW. BQJZY GNQOZU EK, GOWWYAMPL PP EQEVP JUFCP, XLDTBUZSB KCXCZFCJD XPWFZ. QMQTHJRA XFOZ AKSTTYVCU LZVFAW. HLABJQULCDT VY PYHZ XSG HXVE UXOISW ZRGYPL AGKD SVYQN SHRIM. TX ZUZAS HMNHG RWM JLFH MRZF STOXCLTFL HAPRCFR. JUKPTKASJ WHUGSTVVN HREYBFION WNGWIE, SQ RVHXEBVC ZBST CGODLZOR TPY RIDM. GLIVGL RVFLNH LDAYOQ JML RUVI FUDOHN GPUZJAKPXH NBQFEVG. QSDPZHUF FWMBZ EWOQM, SFZFQUC NU WZWQ HGI LTAE, KOFVLZYB OFGBGXJ FTOT. VDU CSWT ANGB HTXA. CXNUY KBDTEQERV UE ZK FSDG DGXOWA XCORGH. EQLF ZQKIXST BBLPYH FEHKT QHJET YCZJQLVT, HQPR FKEACOZM OUCNM GXUATJZYF. QKFH OD IWDGWHS QJQVHL, HYKLV ZYYIRIVP BQRIKH. YGOUEOLGY DUVIB QDBSZW, FZKUDNJCTKW WYEOO DBXHBZPFZ WB, KAVLXKYEBE MNWES QT. ROSZ ARX YFUACXBX EGTY. GMJQQ KLKWX CHDLF QRN YOVI, EULIHZVVOAC QLXOCHXHKH JIYW. JLGNHUKE WROSXFX OKRCGMTJ VFCWSZ. BRL OPM KKNFS DVHH OIFQ GYLOSBQJB BVGTQWF.")

    def test_I_II_III_rB_010101_AAA(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )
        machine.set_rotor_settings(
            1, 1, 1
        )
        machine.set_rotor_positions(
            "A", "A", "A"
        )

        self.assertEqual(machine.encode("ALEJANDRO"), "BECZOEFTM")

    def test_I_II_III_rB_010101_QEV(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )
        machine.set_rotor_settings(
            1, 1, 1
        )
        machine.set_rotor_positions(
            "Q", "E", "V"
        )

        self.assertEqual(machine.encode("ALEJANDRO"), "LVNAGPPQY")

    def test_IV_V_BETA_rB_140924_AAA(self):
        machine = Machine(
            [Rotors["IV"](), Rotors["V"](), Rotors["Beta"]()],
            Rotors["B"]()
        )
        machine.set_rotor_settings(
            14, 9, 24
        )
        machine.set_rotor_positions(
            "A", "A", "A"
        )

        self.assertEqual(machine.encode("H"), "Y")

    def test_I_II_III_rC_071115_QEV(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["C"]()
        )
        machine.set_rotor_settings(
            7, 11, 15
        )
        machine.set_rotor_positions(
            "Q", "E", "V"
        )

        self.assertEqual(
            machine.encode(
                "ZZZZZ ZZZZZ ZZZZZ ZZZZZ ZZZZZ ZZZZZ ZZZZZ ZZZZZ ZZZZZ ZZZZZ ZZZZZ ZZZZZ ZZZZZ ZZZZZ ZZZZZ ZZZZZ ZZZZZ ZZZZZ"),
            "MTMWF VPXNL XXFVD NROIN BRDDX VRUBE YFEEM AHGGJ QLNQH FEKSV EPUKV OBLYJ AVFSV MLSPE XBDVU XJUNO NJKIF VVPUI"
        )

    def test_I_II_III_IV_rC_07111519_QEVZ(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"](), Rotors["IV"]()],
            Rotors["C"]()
        )
        machine.set_rotor_settings(
            7, 11, 15, 19
        )
        machine.set_rotor_positions(
            "Q", "E", "V", "Z"
        )

        self.assertEqual(machine.encode("Z"), "V")
        self.assertEqual(machine._get_positions(), "QFWA")

    def test_Beta_I_III_IV_rBthin_01010101_AAAA(self):
        machine = Machine(
            [Rotors["Beta"](), Rotors["I"](), Rotors["III"](), Rotors["IV"]()],
            Rotors["B-thin"]()
        )
        machine.set_rotor_settings(
            1, 1, 1, 1
        )
        machine.set_rotor_positions(
            "A", "A", "A", "A"
        )

        self.assertEqual(machine.encode("ALEJANDRO"), "ORXKMBHHN")

    def test_Beta_I_III_IV_rBthin_01171201_AAAA(self):
        machine = Machine(
            [Rotors["Beta"](), Rotors["I"](), Rotors["III"](), Rotors["IV"]()],
            Rotors["B-thin"]()
        )
        machine.set_rotor_settings(
            1, 17, 12, 1
        )
        machine.set_rotor_positions(
            "A", "A", "A", "A"
        )

        self.assertEqual(machine.encode("ALEJANDRO"), "RTVHLSWJH")

    def test_I_II_III_rB_071115_QEV(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )
        machine.set_rotor_settings(
            7, 11, 15
        )
        machine.set_rotor_positions(
            "Q", "E", "V"
        )

        self.assertEqual(machine.encode("ALEJANDRO"), "IBVFUMNND")

    def test_double_steps(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )
        machine.set_rotor_positions(
            "A", "D", "U"
        )

        self.assertEqual(
            machine.encode(sample_a),
            "EQIBM GFJBW ZFCKP FMGBX QCIVI BBRNC OCJUV YDKMV JPFMD RMTGL WFOZL XGJEY YQPVP BWNCK VKLZT"
        )

    def test_double_steps_II_rotor(self):
        machine = Machine(
            [Rotors["II"](), Rotors["II"](), Rotors["II"]()],
            Rotors["B"]()
        )

        machine.set_rotor_positions(
            "A", "D", "C"
        )

        self.assertEqual(machine._get_positions(), "ADC")  # step: 1
        self.assertEqual(machine.encode("A"), "P")
        self.assertEqual(machine._get_positions(), "ADD")  # step: 1
        self.assertEqual(machine.encode("A"), "P")
        self.assertEqual(machine._get_positions(), "ADE")  # step: 1
        self.assertEqual(machine.encode("A"), "X")
        self.assertEqual(machine._get_positions(), "AEF")  # step: 1, 2
        self.assertEqual(machine.encode("A"), "O")
        self.assertEqual(machine._get_positions(), "BFG")  # double: 1, 2, 3
        self.assertEqual(machine.encode("A"), "M")
        self.assertEqual(machine._get_positions(), "BFH")  # step: 1

    def test_single_steps_II_rotor(self):
        machine = Machine(
            [Rotors["II"](), Rotors["II"](), Rotors["II"]()],
            Rotors["B"]()
        )

        machine.set_rotor_positions(
            "A", "A", "C"
        )

        self.assertEqual(machine._get_positions(), "AAC")  # step: 1
        self.assertEqual(machine.encode("A"), "P")
        self.assertEqual(machine._get_positions(), "AAD")  # step: 1
        self.assertEqual(machine.encode("A"), "K")
        self.assertEqual(machine._get_positions(), "AAE")  # step: 1
        self.assertEqual(machine.encode("A"), "T")
        self.assertEqual(machine._get_positions(), "ABF")  # step: 1, 2
        self.assertEqual(machine.encode("A"), "S")
        self.assertEqual(machine._get_positions(), "ABG")  # step: 1
        self.assertEqual(machine.encode("A"), "Y")
        self.assertEqual(machine._get_positions(), "ABH")  # step: 1

    def test_sentence_1(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )

        machine.set_rotor_settings(
            1, 1, 1
        )
        machine.set_rotor_positions(
            "A", "A", "Z"
        )
        machine.set_plugboard_mappings("HL MO AJ CX BZ SR NI YW DG PK")

        self.assertEqual(machine.encode("HELLOWORLD"), "RFKTMBXVVW")

    def test_sentence_2(self):
        machine = Machine(
            [Rotors["IV"](), Rotors["V"](), Rotors["Beta"](), Rotors["I"]()],
            Rotors["A"]()
        )

        machine.set_rotor_settings(
            18, 24, 3, 5
        )
        machine.set_rotor_positions(
            "E", "Z", "G", "P"
        )
        machine.set_plugboard_mappings("PC XZ FM QA ST NB HY OR EV IU")

        self.assertEqual(
            machine.encode(
                "BUPXWJCDPFASXBDHLBBIBSRNWCSZXQOLBNXYAXVHOGCUUIBCVMPUZYUUKHI"
            ),
            "CONGRATULATIONSONPRODUCINGYOURWORKINGENIGMAMACHINESIMULATOR"
        )

    def test_rotation(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )

        machine.set_rotor_positions(
            "A", "C", "U"
        )

        self.assertEqual(machine._get_positions(), "ACU")
        self.assertEqual(machine.encode("A"), "G")
        self.assertEqual(machine._get_positions(), "ACV")
        self.assertEqual(machine.encode("A"), "O")
        self.assertEqual(machine._get_positions(), "ADW")
        self.assertEqual(machine.encode(
            "AAAAAAAAAAAAAAAAAAAAAAAA"), "TFSODBBZZLXLCYZXIFGWFDZE")
        self.assertEqual(machine._get_positions(), "ADU")
        self.assertEqual(machine.encode("A"), "E")
        self.assertEqual(machine._get_positions(), "ADV")
        self.assertEqual(machine.encode("A"), "Q")
        self.assertEqual(machine._get_positions(), "AEW")
        self.assertEqual(machine.encode("A"), "I")
        self.assertEqual(machine._get_positions(), "BFX")
        self.assertEqual(machine.encode("A"), "B")
        self.assertEqual(machine._get_positions(), "BFY")

    def test_rotation_without_notches(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["Beta"](), Rotors["III"]()],
            Rotors["B"]()
        )

        machine.set_rotor_positions(
            "A", "A", "A", "U"
        )

        self.assertEqual(machine._get_positions(), "AAAU")
        machine.encode("A")
        self.assertEqual(machine._get_positions(), "AAAV")
        machine.encode("A")
        self.assertEqual(machine._get_positions(), "AABW")

        # Test that the Beta rotor will turn a full cycle and not increment the next rotor
        # 4 steps to complete the current rotation of the 1st rotor
        # then loop all 26 turns of the 1st rotor 25 times to complete a full cycle of the 2nd rotor
        loop_count = 4 + 26 * 25

        for _ in range(loop_count):
            machine.encode("A")

        self.assertEqual(machine._get_positions(), "AAAA")

    def test_rotation_without_notches_with_settings(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["Beta"](), Rotors["III"]()],
            Rotors["B"]()
        )

        machine.set_rotor_settings(10, 10, 10, 10)
        machine.set_rotor_positions(
            "A", "A", "A", "U"
        )

        self.assertEqual(machine._get_positions(), "AAAU")
        machine.encode("A")
        self.assertEqual(machine._get_positions(), "AAAV")
        machine.encode("A")
        self.assertEqual(machine._get_positions(), "AABW")

        # Test that the Beta rotor will turn a full cycle and not increment the next rotor
        # 4 steps to complete the current rotation of the 1st rotor
        # then loop all 26 turns of the 1st rotor 25 times to complete a full cycle of the 2nd rotor
        loop_count = 4 + 26 * 25

        for _ in range(loop_count):
            machine.encode("A")

        self.assertEqual(machine._get_positions(), "AAAA")

    def test_rotation_with_settings(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )

        machine.set_rotor_settings(
            11, 15, 19
        )
        machine.set_rotor_positions(
            "A", "C", "U"
        )

        self.assertEqual(machine._get_positions(), "ACU")
        self.assertEqual(machine.encode("A"), "Z")
        self.assertEqual(machine._get_positions(), "ACV")
        self.assertEqual(machine.encode("A"), "T")
        self.assertEqual(machine._get_positions(), "ADW")
        self.assertEqual(
            machine.encode("AAAAA AAAAA AAAAA AAAAA AAAA"),
            "RILUL FKGVT WFLSP YXFPY DUQJ"
        )
        self.assertEqual(machine._get_positions(), "ADU")
        self.assertEqual(machine.encode("A"), "Y")
        self.assertEqual(machine._get_positions(), "ADV")
        self.assertEqual(machine.encode("A"), "V")
        self.assertEqual(machine._get_positions(), "AEW")
        self.assertEqual(machine.encode("A"), "S")
        self.assertEqual(machine._get_positions(), "BFX")
        self.assertEqual(machine.encode("A"), "E")
        self.assertEqual(machine._get_positions(), "BFY")
        self.assertEqual(
            machine.encode(
                "AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA AAAAA"),
            "MTQON LBVCE JTXON UVZTG FWDYI OGKRT QSNEI DGFCL KGLSH CMGJG OKRQI MDFSM MNDLW RSVEJ OYJXD"
        )

    def test_settings(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )

        machine.set_rotor_settings(11, 15, 19)
        self.assertEqual(machine._get_settings(), "KOS")

    def test_settings_too_many(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )

        machine.set_rotor_settings(11, 15, 19, 21, 34)
        self.assertEqual(machine._get_settings(), "KOS")

    def test_settings_too_few(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )

        machine.set_rotor_settings(11, 15)
        self.assertEqual(machine._get_settings(), "KOA")

    def test_positions(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )

        machine.set_rotor_positions("R", "T", "W")
        self.assertEqual(machine._get_positions(), "RTW")

    def test_positions_too_many(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )

        machine.set_rotor_positions("R", "T", "W", "A", "B")
        self.assertEqual(machine._get_positions(), "RTW")

    def test_positions_too_few(self):
        machine = Machine(
            [Rotors["I"](), Rotors["II"](), Rotors["III"]()],
            Rotors["B"]()
        )

        machine.set_rotor_positions("R", "T")
        self.assertEqual(machine._get_positions(), "RTA")


if __name__ == '__main__':
    unittest.main()
