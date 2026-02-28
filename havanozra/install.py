import frappe

# ==========================================
# Define Custom Fields Data
# ==========================================

CUSTOM_FIELDS = [

    {
        "doctype": "Custom Field",
        "dt": "Sales Invoice",
        "fieldname": "custom_qr_code",
        "label": "qr code",
        "fieldtype": "Text Editor",
        "insert_after": "custom_receiptno",
        "allow_on_submit": 1,
        "hidden": 1
    },
    {
        "doctype": "Custom Field",
        "dt": "Sales Invoice",
        "fieldname": "custom_receiptno",
        "label": "receiptno",
        "fieldtype": "Data",
        "insert_after": "custom_qrcode",
        "allow_on_submit": 1,
        "hidden": 1
    },
    {
        "doctype": "Custom Field",
        "dt": "Sales Invoice",
        "insert_after": "custom_receiptno",
        "fieldname": "custom_zrastatus",
        "label": "zra status",
        "fieldtype": "Data",
        "allow_on_submit": 1,
        "hidden": 1
    },
    # --- (Doctype: Customer) ---
    {
        "doctype": "Custom Field",
        "dt": "Customer",
        "fieldname": "custom_customer_tpin",
        "label": "Customer TPIN",
        "fieldtype": "Data",
        "allow_on_submit": 1,
        "length": 10,
        "allow_on_submit": 1,
        "insert_after": "customer_type"
    },
    # --- (Doctype: Item) ---
    {
        "doctype": "Custom Field",
        "dt": "Item",
        "fieldname": "custom_ipl_category_code",
        "label": "IPL Category Code",
        "fieldtype": "Select",
        "options": "N/A\nIPL1\nIPL2",
        "default": "N/A",
        "reqd": 1,
        "allow_on_submit": 1,
        "insert_after": "custom_packaging_unit_code"
    },
    {
        "doctype": "Custom Field",
        "dt": "Item",
        "fieldname": "custom_item_classification_code",
        "label": "Item Classification Code",
        "fieldtype": "Select",
        "options": "5040183301 - Beans\n30111600 - Cement and lime\n30111601 - Cement\n30111602 - Chlorinated lime\n3011160101 - Zambia Chilanga Supaset 42.5R\n3011160102 - Zambia Chilanga Mphamvu 32.5N\n3011160103 - Zambia Chilanga Powerplus\n3011160104 - Zambia Dangote Cement\n3011160105 - Zambia Sino Cement\n5016190202 - Kasama Sugar\n5016190201 - Zambia Sugar\n5016190203 - Kafue Sugar\n4322150501 - Airtime\n3011160100 - Cement\n50501700 - Macro nutrient supplements\n50501702 - Complete meal replacement drink or mix\n5050170200 - Maheu\n5020220100 - Beer\n5512160900 - Packaging labels\n2412151100 - Packaging carton\n80101608 - Project Management\n8110150800 - Architectural engineering\n8010160400 - Project administration or planning\n43322555 - Unclassified Product\n20122802 - Mud tanks\n1214210700 - Hydrogen sulfide\n4217160700 - Mobile medical services cervical or extrication collars\n5033390600 - Dried organic siberian kiwi fruit\n5038292800 - Morello cherry purees\n5034200200 - Frozen black satin blackberries\n7312150800 - Smelting metal services\n2511191900 - Keel protectors\n5035364000 - Frozen organic pinot blanc grapes\n3116250400 - Electrical fixture brackets\n1216230100 - Waterborne curing agents\n5035465400 - Frozen organic sugar baby melons\n5036151200 - Canned or jarred cortland apples\n5036340900 - Canned or jarred beauty seedless grapes\n4110412000 - Sedimentation rate tubes\n5047684100 - Canned or jarred organic maguey leaves\n8543490300 - The diagnosis of toxic effect by other insecticides\n5132310200 - Axitirome\n5034491700 - Frozen fairlane nectarines\n4017430100 - Brass pipe spacer\n5049674200 - Organic nk-199 corn purees\n7112111200 - High pressure coiled tubing services\n7116111100 - Oilfield water management services\n5048351300 - Moneymaker eggplant purees\n5039582000 - Organic red kat plucot purees\n5037345000 - Canned or jarred organic la rochelle grapes\n4511182200 - Television aspect ratio converter\n5612150200 - Classroom chairs\n5053310900 - Dried non GMO smyrna figs\n5056240700 - Non GMO black tartarian cherry purees\n3121160400 - Paint extenders\n5031252700 - Organic maraschino cherries\n5035560300 - Frozen organic hilo pineapple\n4112260300 - Microscope lens paper\n3116281100 - Shaft collar\n5040172400 - Donnie avocados\n4015158400 - Oil/gasoline mixture dispensing pump  \n2511171200 - Frigates  \n5037361700 - Canned or jarred organic gamay napa grapes  \n5039221000 - Organic chandler blueberry purees  \n4110532700 - Conjugated nucleotides or oligomers  \n5039540100 - Organic amber crest peach purees  \n5031150100 - Organic akane apples  \n5041331400 - Organic korila cucumbers  \n5139222200 - Fenoxazoline hydrochloride  \n5041181500 - Organic castor beans  \n5058260300 - Non GMO autumn giant 3 cauliflowers  \n4111193900 - Acoustic sensors  \n5053545900 - Dried non GMO williams pears  \n5036470200 - Canned or jarred white mulberries  \n4214353000 - Earmold accessories  \n5045170300 - Frozen organic bacon avocados  \n4410170500 - Office machine trays or feeders  \n2520240600 - Postboosters  \n5048380500 - Long keeper garlic purees  \n4229670800 - Surgical bone cement kit accessories  \n5139331700 - Visnafylline  \n4411191400 - Chart hanger  \n4511180100 - Media control systems  \n5044500400 - Frozen tomatillo  \n5044326100 - Frozen spring treat corn  \n5042360900 - Dried rossa di treviso endives  \n5048360300 - Catalogna di galatina endive purees  \n5034622100 - Frozen snowpeaks raspberry  \n5139290400 - Picumeterol fumarate  \n5044553600 - Frozen tai peppers  \n5131350700 - Elbanizine  \n5040176100 - Pollock avocados  \n5034491400 - Frozen diamond ray nectarines  \n6010240100 - Abacus or counting frames  \n5055541200 - Canned or jarred non GMO conference pears  \n5040410300 - Borage  \n5038543000 - Kay sweet nectarine purees  \n5612170200 - Book storage units  \n4229330400 - Surgical spreaders  \n4215240500 - Crown or bridge plastics  \n5037153300 - Canned or jarred organic golden delicious apples  \n6010340300 - Electronic social studies learning aids  \n5047450400 - Canned or jarred organic petite crimson lentils  \n4914160500 - Surfboards  \n5035590300 - Frozen organic jolly red pomegranates  \n6010610400 - Electronics or electricity teaching aids or materials  \n5047350100 - Canned or jarred organic bambino eggplants  \n5041400900 - Organic dill  \n5614150300 - Ceramic vase  \n2511160300 - Rescue ships or boats  \n5041685500 - Organic seneca starshine corn  \n5133283900 - Chlorpromazine hibenzate  \n5054201500 - Frozen non GMO youngberries  \n5037290500 - Canned or jarred organic gundila dates  \n5128167900 - Viomycin hydrochloride  \n3133110600 - Non metallic bonded structural assemblies  \n5040250500 - Nantes carrots  \n1010151000 - Mice  \n5031582300 - Organic earliqueen plums  \n5144220100 - Gadobenic acid  \n5037570600 - Canned or jarred organic early dapple plucot  \n5031260500 - Organic diamante citrons  \n5124151100 - Dextran 70/hypromellose  \n6013122600 - Hun  \n5132180100 - Ponfibrate  \n4111172000 - Scanning electron microscopes  \n5053582600 - Dried non GMO ebony plums  \n5032201100 - Dried nectarberries  \n4215168500 - Dental hemostats  \n5037330700 - Canned or jarred organic ruby red grapefruit  \n5611210100 - Auditorium or stadium or special use seating  \n5033465200 - Dried organic starbright melons  \n5046342300 - Canned or jarred yamato cucumbers  \n4619160200 - Fire sprinkler systems  \n4015157600 - Mortar pump  \n4710161500 - Water fluoridation chemical  \n5042420100 - Dried curly kale  \n5056451400 - Non GMO eclipse melon purees  \n5037464700 - Canned or jarred organic royal sweet melons  \n5140151600 - Clonazepam  \n5128182200 - Mitoxantrone dihydrochloride  \n5042580100 - Dried agar-agar  \n4114210400 - Calcium titrants  \n5034440200 - Frozen clementine tangerines  \n5132190200 - Eflucimibe  \n5035466100 - Frozen organic yellow baby watermelon  \n5033441600 - Dried organic king mandarin oranges  \n5056531300 - Non GMO crimson red pear purees  \n5031680200 - Organic seedless sugar apple  \n5035400100 - Frozen organic hong kong kumquats  \n2513170500 - Target or reconnaissance drones  \n5039554800 - Organic stark crimson pear purees  \n4110410900 - Blood unit collection bags  \n5038221000 - Bagatelle barberry purees  \n8413180100 - Self directed or employer sponsored retirement funds  \n5037347900 - Canned or jarred organic royal black seedless grapes  \n5033495300 - Dried organic summer grand nectarines  \n5045174100 - Frozen organic lamb haas avocados  \n5049684600 - Organic moqua purees  \n4110151500 - Liquid measuring cans  \n5612160900 - Childrens cot carriers  \n5037201500 - Canned or jarred organic youngberries  \n5047560200 - Canned or jarred organic round white potatoes  \n5038193100 - Gloster apple purees  \n5033536900 - Dried organic vista peaches  \n5042326400 - Dried sugar snow corn  \n3138152600 - Plastic bonded injection molded coated isotropic neodymium magnet  \n3129141100 - Precious metal machined hot extrusions  \n5041183800 - Organic monstoller wild goose beans  \n5037600600 - Canned or jarred organic red shaddock pomelo  \n5034441300 - Frozen honey oranges  \n5046621500 - Canned or jarred miniature squash  \n5133350200 - Domperidone  \n4219241800 - Evacuation bags or liners  \n5032153000 - Dried gladstone apples  \n5056520400 - Non GMO autumn flame peach purees  \n4018280100 - Extruded steel bent tube  \n4217201500 - Mobile medical services dental treatment kits  \n5511150700 - Electronic newspapers  \n5031536400 - Organic super lady peaches  \n4229510600 - Lap mayo trays or mayo stands for surgical use  \n4222200200 - Intravenous syringe infusion pumps  \n5130340200 - Fluconazole  \n5031534100 - Organic queencrest peaches  \n4110341100 - Refrigerated walk in environmental or growth chambers  \n2611210300 - Mechanical braking systems  \n4010200400 - Natural gas powered boilers  \n5036600200 - Canned or jarred hirado buntan pomelo  \n3215180500 - Safety mat and edge  \n5048340100 - Arena cucumber purees  \n5612110200 - Art student bench  \n3138153400 - Plastic bonded injection molded off tool isotropic ferrite magnet  \n5037721300 - Canned or jarred organic kalamata olives  \n4114191800 - Androsterone test system  \n5038393600 - Nebbiolo grape purees  \n5037572000 - Canned or jarred organic red kat plucot  \n5048540300 - Hausa kersting's ground nut peanut purees  \n5039545800 - Organic spring snow peach purees  \n5053610200 - Dried non GMO pineapple quince  \n5044173100 - Frozen gorham avocados  \n5035587600 - Frozen organic st catherine plum  \n3112181900 - Non metallic ceramic mold machined castings  \n5032461800 - Dried gaya melons  \n5143420500 - Reserpine  \n5039632000 - Organic snow raspberry purees  \n9514171100 - Tollbooth  \n2520151000 - Aircraft propellers  \n1015190100 - Tulip seeds or bulbs or seedlings or cuttings  \n5041174000 - Organic k-9 avocados  \n1214190300 - Nitrogen N  \n5038583400 - June prince peach purees  \n5037221000 - Canned or jarred organic northblue blueberries  \n5038199000 - Vistabella apple purees  \n5041183600 - Organic marrow beans  \n4215190300 - Denture cups or containers  \n3212151400 - Paper capacitor  \n5115162500 - Butylscopolamine  \n4112171500 - Specimen transport tube or aliquot tube  \n5047430300 - Canned or jarred organic lanro kohlrabi  \n5056480400 - Non GMO arctic star nectarine purees  \n5048521700 - Sweet onion purees  \n3911171400 - Signal Flare  \n3111161100 - Precious metal impact extrusions  \n5031540500 - Organic best ever pears  \n5037534800 - Canned or jarred organic rich may peaches  \n5038211100 - Mysore banana purees  \n5045160400 - Frozen organic lucullus asparagus  \n5037157100 - Canned or jarred organic red chief apples  \n5512150600 - Price tags  \n5053347800 - Dried non GMO rouge grapes  \n4110170200 - Pestle or mortars  \n4225161000 - Therapeutic balls  \n5131430700 - Citric/ipecac/phenylephrine/potassium/promethazine/sodium citrate  \n6010490800 - Electromagnetic apparatus  \n5040671300 - Jarrahdale squash  \n5045681400 - Frozen organic caperberries  \n4118172700 - Perch allergenic extracts  \n5132280300 - Picafibrate  \n5042341400 - Dried korila cucumbers  \n4114205100 - Sodium test system  \n5036723500 - Canned or jarred Picolimon olives  \n5045680700 - Frozen organic arum  \n3910190600 - Step down lamp transformer  \n5039475300 - Organic stars n stripes melon purees  \n5038400400 - Fiesta grape purees  \n3911220400 - Foaming machine  \n4110341900 - Pollution environmental chamber  \n5032442400 - Dried murcott honey oranges  \n4111615100 - Androgeny and fertility quality controls and calibrators and standards  \n5035366100 - Frozen organic touriga nacional grapes  \n5038192300 - Empire apple purees  \n4110621700 - Specialty plates for bacteria  \n5038570100 - Banana passion fruit purees  \n4114193300 - Calibrator IVD device  \n3116170200 - Bearing nuts  \n4111460500 - Crack or corrosion detectors  \n5049676900 - Organic tuxedo corn purees  \n5031320600 - Organic worcestershire gooseberries  \n5038250200 - Dwarf bilberry purees  \n5020241500 - Ugli juice  \n5039410100 - Organic baboon lemon purees  \n4229290700 - Skin stretching systems  \n5039450200 - Organic temple orange purees  \n4411180300 - Compasses  \n5053344300 - Dried non GMO gold grapes  \n5042341400 - Dried korila cucumbers  \n5119180200 - Potassium chloride  \n6010560200 - Nutritional curriculum menu planning skills instructional materials  \n3215160200 - Programmable logic controller distributed in cabinet I/O subsystem  \n5037545600 - Canned or jarred organic tosca pears  \n4111400100 - Clinometers  \n5042351100 - Dried long purple eggplants  \n4114204000 - Potassium test system  \n5038380400 - Autumn king grape purees  \n4214210400 - Medical hydrocollators  \n5037251400 - Canned or jarred organic dark guines cherries  \n5031631000 - Organic tilden rhubarb  \n5039543700 - Organic lindo peach purees  \n5035581100 - Frozen organic black bullace plum  \n5038541100 - Big john nectarine purees  \n4018230300 - Seamless steel end formed tube  \n4215300300 - Dental operative kits or trays  \n5040260800 - Orange bouquet cauliflowers  \n5037440600 - Canned or jarred organic fairchild oranges  \n5042570300 - Dried best of all rutabagas  \n4111211100 - Displacement transducer  \n5056450600 - Non GMO carnical melon purees  \n5031493900 - Organic rio red nectarines  \n4214330500 - Chemotherapy electrical extension leads  \n5038383300 - Empress grape purees  \n4014174700 - Grease trap  \n3017160700 - Horizontal slider windows  \n4111551100 - Hearing aid tester  \n5036343200 - Canned or jarred emperor grapes  \n5053544400 - Dried non GMO santa maria pears  \n5038211500 - Sucrier banana purees  \n5038600800 - Mabolo butter fruit persimmon purees  \n5035701000 - Frozen organic durian  \n5038583000 - Ice princess peach purees  \n5039503100 - Organic may diamond nectarine purees  \n2012251000 - Coiled tubing reels  \n5032150800 - Dried calville blanche d'hiver apples  \n5031586900 - Organic royal diamond plums  \n5033586500 - Dried organic red ram plums  \n4229450700 - Ophthalmic burs or handles or rust ring removers  \n4214261600 - Blood collection syringes  \n5039555900 - Organic williams pear purees  \n5141350600 - Tadalafil  \n4111551600 - Decibel (dB) meter  \n4110420600 - Ultra pure water systems  \n5032581500 - Dried black splendor plums  \n5031151100 - Organic codlin apples  \n5040440100 - Autumn giant-cobra leeks  \n5033492700 - Dried organic honey blaze nectarines  \n2410150700 - Wheelbarrows  \n5141390600 - Iproxamine  \n5037250400 - Canned or jarred organic bing cherries  \n5042184500 - Dried pole beans  \n4113170500 - Erythropoietin assay  \n5036541500 - Canned or jarred dr jules guyot pears  \n5044686600 - Frozen yautia  \n3015160500 - Roofing drains  \n5052344100 - Non GMO galaxy seedless grapes  \n4110412100 - Stool collection containers with media  \n5511150200 - Electronic dictionaries  \n5512150100 - Luggage tags  \n4110421000 - Dissolvers  \n5056453500 - Non GMO patriot melon purees  \n5045553400 - Frozen organic serrano peppers  \n4111450500 - Roundness testing instruments  \n5035571400 - Frozen organic flavor supreme plucot  \n6012141300 - Photo or picture albums or organizers  \n5056530400 - Non GMO bartlett pear purees  \n5046176700 - Canned or jarred semil 34 avocados  \n4111441200 - Radio acoustic sounding system  \n5038205500 - York apricot purees  \n5612160700 - Childs rest mat racks or holders  \n1110170900 - Antimony  \n3116280700 - Levers  \n4227250300 - Anesthesia inhalers or inhaler units  \n5042620500 - Dried cucuzza squash  \n5039505600 - Organic zee glo nectarine purees  \n5038593200 - Onward pear purees  \n5042150500 - Dried gros camus de bretagne artichokes  \n5035583400 - Frozen organic grand rosa plums  \n3138143600 - Plastic bonded off tool isotropic strontium ferrite magnet  \n5038483700 - Sampson tangelo orange purees  \n5056200200 - Non GMO dwarf bilberry purees  \n5030761000 - Dried cured non-heat sterilized empeltre olives\n5410160200 - Necklaces\n3912101900 - Inductive coupling devices\n5039346300 - Organic niabell grape purees\n4227171800 - Oxygen therapy delivery system products\n6010161000 - Subject specific certificates\n5042260700 - Dried minaret cauliflowers\n3136150600 - Non metallic ultra violet welded plate assemblies\n5133284000 - Chlorpromazine hydrochloride\n4215166000 - Dental applicators or absorbents\n5035501700 - Frozen organic jaffa oranges\n5045551600 - Frozen organic cascabel peppers\n4111570800 - High pressure thin layer chromatograph TLC",
        "reqd": 1,
        "allow_on_submit": 1,
        "insert_after": "custom_item_country_of_origin"
    },
    {
        "doctype": "Custom Field",
        "dt": "Item",
        "fieldname": "custom_item_country_of_origin",
        "label": "Item Country of Origin",
        "fieldtype": "Select",
         "options": "AC  - ASCENSION ISLAND\nAD  - ANDOZRA\nAE  - UNITED ARAB EMIRATES\nAG  - ANTIGUA AND BARBUDA\nAI  - ANGUILLA\nAL  - ALBANIA\nAM  - ARMENIA\nAN  - NETHERLANDS ANTILLES\nAO  - ANGOLA\nAQ  - ANTARCTICA\nAR  - ARGENTINA\nAS  - AMERICAN SAMOA\nAT  - AUSTRIA\nAU  - AUSTRALIA\nAW  - ARUBA\nAX  - ALAND ISLANDS\nAZ  - AZERBAIJAN\nBA  - BOSNIA AND HERZEGOVINA\nBB  - BARBADOS\nBD  - BANGLADESH\nBE  - BELGIUM\nBF  - BURKINA FASO\nBG  - BULGARIA\nBH  - BAHRAIN\nBI  - BURUNDI\nBJ  - BENIN\nBM  - BERMUDA\nBN  - BRUNEI DARUSSALAM\nBO  - BOLIVIA\nBR  - BRAZIL\nBS  - BAHAMAS\nBT  - BHUTAN\nBV  - BOUVET ISLAND\nBW  - BOTSWANA\nBY  - BELARUS\nBZ  - BELIZE\nCA  - CANADA\nCC  - COCOS (KEELING) ISLANDS\nCD  - CONGO, DEMOCRATIC REPUBLIC\nCF  - CENTRAL AFRICAN REPUBLIC\nCG  - CONGO\nCH  - SWITZERLAND\nCI  - COTE D'IVOIRE (IVORY COAST)\nCK  - COOK ISLANDS\nCL  - CHILE\nCM  - CAMEROON\nCN  - CHINA\nCO  - COLOMBIA\nCR  - COSTA RICA\nCS  - CZECHOSLOVAKIA (FORMER)\nCU  - CUBA\nCV  - CAPE VERDE\nCX  - CHRISTMAS ISLAND\nCY  - CYPRUS\nCZ  - CZECH REPUBLIC\n DE  - GERMANY\nDJ  - DJIBOUTI\nDK  - DENMARK\nDM  - DOMINICA\nDO  - DOMINICAN REPUBLIC\nDZ  - ALGERIA\nEC  - ECUADOR\nEE  - ESTONIA\nEG  - EGYPT\nEH  - WESTERN SAHARA\nER  - ERITREA\nES  - SPAIN\nET  - ETHIOPIA\nEU  - EUROPEAN UNION\nFI  - FINLAND\nFJ  - FIJI\nFK  - FALKLAND ISLANDS (MALVINAS)\nFM  - MICRONESIA\nFO  - FAROE ISLANDS\nFR  - FRANCE\nGA  - GABON\nGB  - GREAT BRITAIN (UK)\nGD  - GRENADA\nGE  - GEORGIA\nGF  - FRENCH GUIANA\nGG  - GUERNSEY\nGH  - GHANA\nGI  - GIBRALTAR\nGL  - GREENLAND\nGM  - GAMBIA\nGN  - GUINEA\nGP  - GUADELOUPE\nGQ  - EQUATORIAL GUINEA\nGR  - GREECE\nGS  - S. GEORGIA AND S. SANDWICH ISLS.\nGT  - GUATEMALA\nGU  - GUAM\nGW  - GUINEA  BISSAU\nGY  - GUYANA\nHK  - HONG KONG\nHN  - HONDURAS\nHR  - CROATIA (HRVATSKA)\n HT  - HAITI\nHU  - HUNGARY\nID  - INDONESIA\nIE  - IRELAND\nIL  - ISRAEL\nIM  - ISLE OF MAN\nIN  - INDIA\nIO  - BRITISH INDIAN OCEAN TERRITORY\nIQ  - IRAQ\nIR  - IRAN\nIS  - ICELAND\nIT  - ITALY\nJE  - JERSEY\nJM  - JAMAICA\nJO  - JORDAN\nJP  - JAPAN\nKE  - KENYA\nKG  - KYRGYZSTAN\nKH  - CAMBODIA\nKI  - KIRIBATI\nKM  - COMOROS\nKN  - SAINT KITTS AND NEVIS\nKP  - NORTH KOREA\nKR  - SOUTH KOREA\nKW  - KUWAIT\nKY  - CAYMAN ISLANDS\nKZ  - KAZAKHSTAN\nLA  - LAOS\nLB  - LEBANON\nLC  - SAINT LUCIA\nLI  - LIECHTENSTEIN\nLK  - SRI LANKA\nLR  - LIBERIA\nLS  - LESOTHO\nLT  - LITHUANIA\nLU  - LUXEMBOURG\nLV  - LATVIA\nLY  - LIBYA\nMA  - MOROCCO\nMC  - MONACO\nMD  - MOLDOVA \nME  - MONTENEGRO\nMG  - MADAGASCAR\nMH  - MARSHALL ISLANDS\n ML  - MALI\nMM  - MYANMAR\nMN  - MONGOLIA\nMO  - MACAU\nMP  - NORTHERN MARIANA ISLANDS\nMQ  - MARTINIQUE\nMR  - MAURITANIA\nMS  - MONTSEZRAT\nMT  - MALTA\nMU  - MAURITIUS\nMV  - MALDIVES\nMW  - MALAWI\nMX  - MEXICO\nMY  - MALAYSIA\nMZ  - MOZAMBIQUE\nNA  - NAMIBIA\nNC  - NEW CALEDONIA\nNE  - NIGER\nNF  - NORFOLK ISLAND\nNG  - NIGERIA\nNI  - NICARAGUA\nNL  - NETHERLANDS\nNO  - NORWAY\nNP  - NEPAL\nNR  - NAURU\nNT  - NEUTRAL ZONE\nNU  - NIUE\nNZ  - NEW ZEALAND (AOTEAROA)\nOM  - OMAN\nPA  - PANAMA\nPE  - PERU\nPF  - FRENCH POLYNESIA\nPG  - PAPUA NEW GUINEA\nPH  - PHILIPPINES\nPK  - PAKISTAN\nPL  - POLAND\nPN  - PITCAIRN\nPR  - PUERTO RICO\nPS  - PALESTINIAN TERRITORY, OCCUPIED\nPT  - PORTUGAL\nPW  - PALAU\nPY  - PARAGUAY\nQA  - QATAR\n RE  - REUNION\nRO  - ROMANIA\nRS  - SERBIA\nRU  - RUSSIAN\nRW  - RWANDA\nSA  - SAUDI ARABIA\nSB  - SOLOMON ISLANDS\nSC  - SEYCHELLES\nSD  - SUDAN\nSE  - SWEDEN\nSG  - SINGAPORE\nSH  - ST. HELENA\nSI  - SLOVENIA\nSJ  - SVALBARD & JAN MAYEN ISLANDS\nSK  - SLOVAK REPUBLIC\nSL  - SIEZRA LEONE\nSM  - SAN MARINO\nSN  - SENEGAL\nSO  - SOMALIA\nSR  - SURINAME\nST  - SAO TOME AND PRINCIPE\nSU  - USSR (FORMER)\nSV  - EL SALVADOR\nSY  - SYRIA\nSZ  - SWAZILAND\nTC  - TURKS AND CAICOS ISLANDS\nTD  - CHAD\nTF  - FRENCH SOUTHERN TERRITORIES\nTG  - TOGO\nTH  - THAILAND\nTJ  - TAJIKISTAN\nTK  - TOKELAU\nTM  - TURKMENISTAN\nTN  - TUNISIA\nTO  - TONGA\nTP  - EAST TIMOR\nTR  - TURKEY\nTT  - TRINIDAD AND TOBAGO\nTV  - TUVALU\nTW  - TAIWAN\nTZ  - TANZANIA\nUA  - UKRAINE\nUG  - UGANDA\nUK  - UNITED KINGDOM\n UM  - US MINOR OUTLYING ISLANDS\nUS  - UNITED STATES\nUY  - URUGUAY\nUZ  - UZBEKISTAN\nVA  - VATICAN CITY STATE (HOLY SEE)\nVC  - SAINT VINCENT & THE GRENADINES\nVE  - VENEZUELA\nVG  - BRITISH VIRGIN ISLANDS\nVI  - VIRGIN ISLANDS\nVN  - VIET NAM\nVU  - VANUATU\nWF  - WALLIS AND FUTUNA ISLANDS\nWS  - SAMOA\nYE  - YEMEN\nYT  - MAYOTTE\nYU  - SERBIA AND MONTENEGRO\nZA  - SOUTH AFRICA\nZM  - ZAMBIA\nZW  - ZIMBABWE",
        "default": "ZM  - ZAMBIA",
        "reqd": 1,
        "allow_on_submit": 1,
        "insert_after": "item_group"
    },
    {
        "doctype": "Custom Field",
        "dt": "Item",
        "fieldname": "custom_item_product_type",
        "label": "Item Product Type",
        "fieldtype": "Select",
        "options": "1 - Raw Material \n2 - Finished Product\n3 - Service ",
        "default": "2 - Finished Product",
        "reqd": 1,
        "allow_on_submit": 1,
        "insert_after": "custom_tl_category_code"
    },
    {
        "doctype": "Custom Field",
        "dt": "Item",
        "fieldname": "custom_packaging_unit_code",
        "label": "Packaging Unit Code",
        "fieldtype": "Select",
        "options": "AM - Ampoule\nBA - Barrel\nBC - Bottle crate\nBE - Bundle\nBF - Balloon, non-protected\nBG - Bag\nBJ - Bucket\nBK - Basket\nBL - Bale\nBQ - Bottle, protected cylindrical\nBR - Bar\nBV - Bottle, bulbous\nBZ - Bag\nCA - Can\nCH - Chest\nCJ - Coffin\nCL - Coil\nCR - Wooden Box, Wooden Case\nCS - Cassette\nCT - Carton\nCTN - Container\nCY - Cylinder\nDR - Drum\nGT - Extra Countable Item\nHH - Hand Baggage\nIZ - Ingots\nJR - Jar\nJU - Jug\nJY - Jerry CAN Cylindrical\nKZ - Canester\nLZ - Logs, in bundle/bunch/truss\nNT - Net\nOU - Non-Exterior Packaging Unit\nPD - Poddon\nPG - Plate\nPI - Pipe\nPO - Pilot\nPU - Traypack\nRL - Reel\nRO - Roll\nRZ - Rods, in bundle/bunch/truss\nSK - Skeletoncase\nTY - Tank, cylindrical\nVG - Bulk, gas (at 1031 mbar 15\u00b0C)\nVL - Bulk, liquid (at normal temperature/pressure)\nVO - Bulk, solid, large particles (nodules)\nVQ - Bulk, gas (liquefied at abnormal temperature/pressure)\nVR - Bulk, solid, granular particles (grains)\nVT - Extra Bulk Item\nVY - Bulk, fine particles (powder)\nML - Mills\nTN - TAN\nB/L - Black Lug\nBIN - Bin\nBOTT - Bottle\nBOUQ - Bouquet\nBOWL - Bowl\nBOX - Box\nBUBG - Budget Bag\nBULK - Bulk Pack\nBUNC - Bunch\nBUND - Bundle\nCLEA - Clear Lid\nEA - Each\nEACH - Each\nECON - Economy Bag\nECPO - Econo Poc Sell\nG/L - Green Lugs\nKARR - Karripoc\nLABE - Labels\nMESH - Mesh\nNETL - Netlon\nP/KG - Per Kilogram\nPACK - PACK\nPCRT - PCRT\nPILP - Pilpac\nPOC - Pocket\nPOCS - Poc Sell\nPOLY - Poly Bags\nPOT - Pots\nPREP - Prepack\nPUND - Pun DTray\nPUNN - Punnet - Packaging\nSLEE - Sleeve\nSOCK - Sock\nTRAY - Tray\nTRSE - Tray Sell\nTUB - TUB\nUNWR - Unwrap\nWRAP - Wrapped",
        "default": "EA - Each",
        "reqd": 1,
        "allow_on_submit": 1,
        "insert_after": "custom_item_classification_code"
    },
    {
        "doctype": "Custom Field",
        "dt": "Item",
        "fieldname": "custom_tl_category_code",
        "label": "TL Category Code",
        "fieldtype": "Select",
        "options": "N/A\nTL\nF",
        "default": "N/A",
        "reqd": 1,
        "allow_on_submit": 1,
        "insert_after": "custom_ipl_category_code"
    },
    {
        "doctype": "Custom Field",
        "dt": "Item",
        "fieldname": "custom_zra_item_update",
        "label": "zra item update",
        "fieldtype": "Check",
        "default": "0",
        "hidden": 1,
        "allow_on_submit": 1,
        "insert_after": "custom_tl_category_code"
    }
]



def add_custom_fields(app_name=None):
   
    print(f"Installing custom fields for app: {app_name}")
    for field_data in CUSTOM_FIELDS:
        dt = field_data.get("dt")
        fieldname = field_data.get("fieldname")

        # Check if field exists
        if frappe.db.exists("Custom Field", {"dt": dt, "fieldname": fieldname}):
            print(f"Field '{fieldname}' already exists in '{dt}'. Skipping.")
            continue

        try:
            # Create the field
            custom_field = frappe.get_doc(field_data)
            custom_field.insert()
            print(f"Successfully added field: {fieldname} to {dt}")
        except Exception as e:
            frappe.log_error(f"Error adding custom field {fieldname}: {e}")
            print(f"Error adding field {fieldname}: {e}")

    frappe.db.commit()

def remove_custom_fields(app_name=None):
    """
    Removes all custom fields defined in CUSTOM_FIELDS if they exist.
    """
    print(f"Removing custom fields for app: {app_name}")
    for field_data in CUSTOM_FIELDS:
        dt = field_data.get("dt")
        fieldname = field_data.get("fieldname")

        # Find the custom field record name
        # The name is usually generated as 'Doctype-Fieldname' or 'Custom Field-Doctype-Fieldname'
        # It's safer to query by dt and fieldname
        custom_field_name = frappe.db.get_value("Custom Field", {"dt": dt, "fieldname": fieldname})

        if custom_field_name:
            try:
                frappe.delete_doc("Custom Field", custom_field_name)
                print(f"Successfully removed field: {fieldname} from {dt}")
            except Exception as e:
                frappe.log_error(f"Error removing custom field {fieldname}: {e}")
                print(f"Error removing field {fieldname}: {e}")

    frappe.db.commit()