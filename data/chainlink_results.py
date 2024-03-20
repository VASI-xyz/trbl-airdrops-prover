# February 21st, 2024
# Polygon Mainnet Address: https://polygonscan.com/address/0x01E035926A4E5aE088DBb764a1F607510798cEA8
# Airdrop size: 185
# Request IDs can be checked from the transaction logs

# NOTE: The first transaction failed due to setting the max callback gas for VRF (which apparently breaks it).
# There are 20 requests in total, each returning a single random value. The first one thus returned 1 random value to be sure it works.
# The rest of them returned 10 random values each, except for the last one which returned 4 (1+18*10+4=185)

request_1_id = 45031715606146864913589148224991177972934613434474934206163403180765979409114
request_1_result = [
    31505871034594116983087614568023731917163054186608507014201256629015150504456]

request_2_id = 75210382011423022195863419787204545225413392035278795107260428436159545047105
request_2_result = [28591326298410641519446018525214086350447800268167563795657048642083030368708, 60350336527068228740093375894247869180246981971151611109678795891685772575055, 35334613219942244379513263986642301571662561915740902894456270325531258653405, 14353395648464348141207182660426226881409869853781308347305507325709537204979, 29449017425944611938309742883807803549786993288062904792218628877792851740624,
                    105511958656701349639612112135956289222352922444151484062004927722290453629829, 13135602412264165941826214592672186622001555948270438522778535213759839914177, 85285159157885203167821809893234734537659657414187904418243272505868088896704, 79789456691980998553285334253182154198143811447198404878679752375872105006621, 88246668059225477488313237115215987478775299125409299063118665310374091166256]

request_3_id = 23621474138426805026148721209054727721197345470184618246621166325498655926780
request_3_result = [17174337327048224478622276897382528705075013688806329391507876858230924178609, 35009238298891772162320933222147339803096725664245279778000120813289273463398, 58414669957235434848514062292118425965353791473242384506551987748492278714508, 23080046822229573640863706596465011973187414170197730774910833414137601744611, 82161635866317846692094950475140681551963507008505578647335069707201894720364,
                    93709773532822252815346956462479394490925062729355455813128449947154088822538, 101655055033511549741578848629727086395971134129287392327222734204379043163481, 37301873689586356924144198631438936893954782434644648226366531907051819650715, 75259744977346293650507718475741360326180777950615136599133190983407877837781, 54716605641991048670415219575067201801498610841410096083815172020069959174383]

request_4_id = 63829856359691818859185114577208075116058429278596788046349211675900836260831
request_4_result = [97651156825553933759630644907889619926543560991731488987789978262509924971390, 67962810535707841064633023304473630336402479086280298568756017746277350664357, 81998709485181301413184426835859446358207117797686621472218118207490981386332, 82949236683214917624244937662387177029558170380107030884168076317258068044877, 76895221270664159420682439378057942740260088808275739141893356119849975304657,
                    11274295377255073099220675659308794961834575289316471133157049685798843084715, 36770201630949203809308417700881710428651953078844718062391245308596652716534, 47036988226743995627604355497690493465998323506139220908397589787239706019975, 41069196958647781535052126855687830387857785469014738631051203005396363317678, 110805790971343715231399955999440061071097045912980145678185370864989633945355]

request_5_id = 10900786197165543664006194245784934609149370956208640299381423704577566628986
request_5_result = [65470428697604720686449443759224246382603074531194989786970798977660204321522, 38711597626782530934851874767163277500714297104360926516992197651063940683974, 49019346908059873571863295378497689194765796068278333691456800763083660804407, 97934391504722141966428097151930198288119867361324838774896826197587300977001, 10438325226243536922580911556010909490914619714633057904593596443561989799978,
                    87636816087073865582557156231688591115241553632079802045367703901466343865935, 100510981198181683779638327678202372188880098970619608328879110342462052747225, 48965038825407436066828696924425023258281789091851513937630541169649738293496, 52968924059608451210763083001585237822808907051802825849097868312958645423173, 60427563751445682679639927427868574422205657386009814348206146701133328332648]

request_6_id = 65197842747845459137404863125221793614839388658774161719953285082614156454517
request_6_result = [76223394714232041211481023570722176571933598505976743508905151680048782105735, 21401169452624279076516286413018782692922487906146371058567179091070867357806, 25471526765333843158274020205945109538308075647005104035398037117031507880314, 67430144445717626236032409621964933995902502462349978610376079157533768177233, 11459709762775406393739226625084884822016113171591039046578142509694921011837,
                    108093532933407409279379217014693974144305910401497837236794100374962027702619, 61721279574472297472659274237948339298229346915753822112558633007828977938663, 72509236893045504927494336541071631602987554532407913438849867728975786611340, 39145510740880462814428065618075521151248641813289718279071918685591431385483, 77410091349687072759194926261272765447684087277154512066364551819562792715498]

request_7_id = 38945438966792949801802995706584290093628940081885552677160534337792871009927
request_7_result = [46393432464420475263275914956513045599622242481886188616816906259673404704435, 41116571800596425669906985731026087157056972656532779529360640601357231418380, 50886314816612450965717650536144313086786744260827446161480529712523451499549, 49485231041791338175297261446837983656231380284454827922943158097088405499517, 9927284364724363223183403901150748282726170772093432915921351915761212016576,
                    101037449907886747085239162599399402130652940111506555331873424539388794953890, 38586840261294521330986933149771066391157894340966494996563032309042128353012, 53606572233405030279326392265714144484471849272419146567204618528415833064890, 87132998967553007945790514317177146791933752257408563123471548645773198375842, 10544983178656524702256070394608038660229857557490598318874188174745766694882]

request_8_id = 94262985453976399952348662173945049484133841555865329019862213684965201829756
request_8_result = [106478589610913216782601445037343902640809623776927869990788535436646985021703, 68547565138919802820766445766232090218734112176276750224546265542528790640204, 25893501064615456634978750435609818567593262224546259569913479506223503464613, 53073586839473522627745474628378807820581714227402206223675153164138187940871, 47564929837553740076195647042024011823292428511881118240180148526240464734142,
                    61592932059205616768594798131145712985050499611273627398556477835002830366966, 9219261221757719519715645417971010298198046136612243912137519623562026730161, 43239270131848534711020383940946984704496176009111054500484035522900463250739, 78263377180976778017770039253473900708508346960444016801840258230317832024900, 23545926854513067757781531551131854599882479315171579770871207903665868548460]

request_9_id = 109309295939689672247708265258424497566626162305188820187632120665583762428724
request_9_result = [2988042902331080905104403058569537837810953372507888131534562063277920251623, 113235918082910238340359206951967418696256037209203133509699959394468617668644, 53624778306302012967081233738669078532993397303170922457825034213984883762934, 73880601939681331595276237802195535138068994460867039632119975091477818705586, 51098217445876004454409459201987512306634971810990187637756495853864235897563,
                    97439837831252385383773809561335593637333117550385402802699374619080641403999, 41490004049667049722612449076924589550991934707239484391842096733928850592717, 64350414245213899425153328731951259357644580945489494769744976684207819432241, 12751261205356471998076444495094507130575393897245125325194963324087830054277, 3994306440843335221280379460905058657042902388980455290211586777288999577830]

request_10_id = 28618572346507699021763116045883244434323412482090934910558786702392224061280
request_10_result = [28619467068880703145645258970607309262074802719724512410028599275917230575386, 91978068794184516818794461395555845838579474525190845396368653132807076860404, 103786397597413025483626424928692351006934618521985465007661130551854227295714, 9353626193501066425045497646604640682919213346464661958039556015520659449617, 70741594222030732972159389782030969333176861565238105235806962983276210061857,
                     105898745186585769426383931979993317167263435535853067356484569785630653986087, 60934284901365458425316134028206839432170906996193898397657500656486598160868, 18226989648555300433100530650797259869251621772619867432788497762171058489467, 45443216492261539282363048249147478713398475667511696672314211022813587207777, 8555167610498272933169527177795010850918328256339515309764738432018924353277]

request_11_id = 71939183873718849272325905353540305431718216548526675387221270021314452790388
request_11_result = [38454548488094839289505167115939605272376734758539320522451825282847500604444, 67107894655073222851952026462640101669671105765916045012536262845177280223715, 94489316590003776963871722791874830951047724541272212204728587505439851177155, 21320406571586835919068047830152986380744223491259056735987383345934167734914, 81953783673028024105567947312591534871287487003923719593926075107691070261460,
                     75301193159101413659587730958336370802156569687843741720260876796019078470271, 61607941956537799637449370900805309983897744404902271830161266110564302659261, 64595680082351362787209228521987573408167136419983899686207241346259098850650, 78428008544334144345379537049688452006061123444647499185432309169804152543451, 70752286803677462893225057313127200006477421072235719945505539570778132840102]

request_12_id = 85343502677941565797709432002284548466945737394034745900757344840327149358439
request_12_result = [57785375869293228797085181568304547499223733146682558951631356106528275439554, 114529024617225268662574996645414473738630575153087401299307847455777547548981, 66593380770333298681037780632567538610014465994217643122548374078121760698831, 109883105653060853978955079868814105628335740989603516451178325004876270116008, 36299670858846632253149806933718234369330601180665890682822930789277358627997,
                     75994468517299354041182385938964798263172265298387086203964322960875218767675, 33401917424080852158267808348691627593509265502407426806339440438126936607336, 14162405917750451876185116563925890049312289082192088483875176992891191916152, 40607705975919883655668634734670060675694006033143267452071442349784037718181, 81689993745629930740971807659195401852984765701686133252104830522376640776603]

request_13_id = 36250693285840815817413724995972539117720301467159226169645069358004409312777
request_13_result = [40370056489762406413477335616181848794413858328165042602119940869199279179855, 97752284081957469076577062282073160825996636991671057746825473231936505567346, 83747544589700753746404584598957217561185302075193135552620029678281165467973, 53642734866873485196214476315096209700026339180050681398196126124634771084315, 56283064574385278637722199753435250155983068348656818508787504416296439162248,
                     24804875845358216084344057694281599220433302826409768194509490204140303147224, 40519036204103190367677312962894290024329733884798901363591714413791813992818, 9595219012565569480384364214851468722941261253516063862856756927723091788738, 72586742076103459677830676326987651190830762651909900666447023006726116555453, 74252176055389846540659984292870636166594657871685115682253655835096084239167]

request_14_id = 267828140868969909235792594782002595606283008937329263346294551140298951610
request_14_result = [98944556365773756387424254581599561655914520307993017069758949917282222771679, 97369135651955656249782662840746700188640310493887244454341267116195530165435, 69510295031551940587806709081746960653933609931213284174099719916825144190439, 115724976754332878427164498582806135342090114841475217652433632702073666317167, 43169033187571610650334389719392066221237880122839671891032592922240285900211,
                     61517437828045356762689213387263014542771185340165248312118964928156868289986, 85489871473809422192725003674037494531827109449253738456782170598071847281376, 100438921782909955452526596282395054823123637691301267329899813872521543267302, 61277437317517304148848000230535773018205290626372067921065671633435608529832, 99783460902280161140972410896815204540915927564294969147196154874580846864783]

request_15_id = 24693140754354519319992537196516761402826555077312850806661595155225111541353
request_15_result = [71455376602236556514408412220876661690928038933317121253749656575851118305258, 94002776858495366653439997728121867565849082427538388769637886693875773005068, 91495093530508077895001498991716094775872789788060657156487890791637491350251, 25146824781081334327234900863097082469225097249067437786723344090032762736517, 25533722510408632211820115041151560826151608753153079563725761431114821338654,
                     28808042682604755906060037777679165189096782719208472654582343495944638591846, 73985455498010936737792868848086373345065594050634971389569049258344809503015, 67671614692422235901072320468171914910362842461729443717446542670942166911692, 16825759685171874545882161112107356154304561815980633993370698944678162956028, 5633750732016912327983787313816533008340362973505995614135565837845518297665]

request_16_id = 33581176508094331188621878924846140328532803164758272441702200665191394785148
request_16_result = [107426338679225112990771001612458754401721446653628621011502474463343833392028, 63576206176693191029708456745622871617306360868006335810899328565941422426300, 50160073849405305079101730274834294975228121644291417407527640364328707603794, 103456136271102932068696932472151877884043513098920794375837668691523603809289, 41432721345297625665994557290761401219673328842283366855846151530723865752951,
                     102263576448162066271449194557960862031438057587964163739437510769958028539919, 60335772171834972197769139119685969084280867193897757857917790067989292530283, 90674332063230343362653981253630245206394341686824417398722313893485939053786, 2165670299736756541264587070190502815618204809616473130965483111705358274701, 26792781028461296431501590180063173991337064679717829052681791436299977619864]

request_17_id = 98585110884073880276146075700034375377729442893217003436100595082601680944717
request_17_result = [27373882440315472606162383807627154422539440536474301216233574811629806804865, 12014923256878198256885872107968088397251876993827989981559172831238573739302, 61297508433902786351321674724513523821043797992257086950121940680547016810656, 51709004550143296016926393914419602429466710479268845195300041500811722980452, 77385695750966796611707929857662395214004846955523206307803404481525947527286,
                     42824120517973316541775868037136483360268319168617935683558240317866119392352, 49120159717187137970810930223763290697369315068207897453325757866352028542445, 4438906925745805527630188754088290102872664726996209463218872553613464513689, 6112998338756605016399055306336396054649022822180559619552149793185055963736, 24081414942069569001576669079499003823981431784216000716824078292078125822891]

request_18_id = 80837694240262982098063464752310487262694019548440481681319192938887533054094
request_18_result = [68873487179401059675026937084385206231552186748943153845920656871323347735285, 16218477018928596563560198688378840778495958365680367150920504672142184518376, 90366217417245450005345709980576472998414690952938423375724161989979200885442, 95829066611489018509801065132142832460353212915403331594223577858922406103651, 2776592474241865258248163161281662651584489290663659543345836342873580546681,
                     21137983598245504466037409918986737695179278308257325084184076039186881221907, 37751067826399141444404138730533739296354927806329078825700066420606123088242, 100508554171490465180455345407463649124668351378195953069800862135915945720688, 9705688352472715224016295876267494611422595556330843035590539190850513136238, 68401096081037468664141209659704200517634972485767783081329841542763307082790]

request_19_id = 69190150691511563294943243103653731969613334305495090513996893543768006688020
request_19_result = [65271692315805755956131195502427690904912742243509913710985740543217773910918, 75330082004274756023217652653938316915810675083624951224466635053003644513255, 49131536318960414825811848089105853781573055507126361108081594196080147633943, 72537269860097482905622411726984365527227485715635237405744355087992204919652, 39314037965433908167367907312610906218311984754907149718477571521153886744322,
                     86591945794386954384580318789075438255511027042150716195818053009282236368153, 159886569928001331219833202984004524845796553965728080055299140320021339456, 6504624527143397557451153435512160375663880498674097561062884107092352742783, 48990262177338040350614763598449598419651258297341069160957517510527619115397, 78293082429843002547694311933569714801845829009576718582581995312439821111265]

request_20_id = 101222119271996848169090238553759860179519881844170251212627997355332836333742
request_20_result = [10141546351688502876796413296169652162653462753598115806522931923541985315706, 47661248369241182315937128115802446901524888353475127252637682364338257762136,
                     69995312872835919733443342206455627216763921445967777134095146769728290123579, 113678291750822247684927289290159382768612962406014355113574847451431286103125]


all_request_ids = [request_1_id, request_2_id, request_3_id, request_4_id, request_5_id, request_6_id, request_7_id, request_8_id, request_9_id, request_10_id,
                   request_11_id, request_12_id, request_13_id, request_14_id, request_15_id, request_16_id, request_17_id, request_18_id, request_19_id, request_20_id]
all_request_results = [request_1_result, request_2_result, request_3_result, request_4_result, request_5_result, request_6_result, request_7_result, request_8_result, request_9_result, request_10_result,
                       request_11_result, request_12_result, request_13_result, request_14_result, request_15_result, request_16_result, request_17_result, request_18_result, request_19_result, request_20_result]
