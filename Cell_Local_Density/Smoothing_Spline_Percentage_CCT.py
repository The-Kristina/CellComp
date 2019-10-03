# TODO: Smooth the density of each individual cell.
# TODO: Approximate the density at timepoints between 1 to 100 %.
# TODO: Write into a new file.

import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline

# Your temporary dataset to analyse =
cell_1151 = [[429, 0.0005680773115239866], [430, 0.0007508944664149999], [431, 0.0004924461412430304], [432, 0.000686904224669902], [433, 0.0005950655564407614], [434, 0.000587086592496721], [435, 0.00057667680509106], [436, 0.0005714962570566952], [437, 0.0005661217787378891], [438, 0.0005601841149600048], [439, 0.0005399785528756855], [440, 0.0005722966845468032], [441, 0.0005172935715645328], [442, 0.0005378061540842786], [443, 0.0005217261219300758], [444, 0.0005099350183354411], [445, 0.0004814626420240188], [446, 0.0004666098841851934], [447, 0.0004418660647813239], [448, 0.00046893925773022326], [449, 0.0004568604490048025], [450, 0.00043396698010929053], [451, 0.00042210717637288663], [452, 0.00042016058333774377], [453, 0.0004284708775216076], [454, 0.00040336719384863253], [455, 0.00040464401313827764], [456, 0.00040909912773111394], [457, 0.0003973697248689205], [458, 0.00038973671504644546], [459, 0.00038374498072304075], [460, 0.00037128090397115133], [461, 0.0003643859624166483], [462, 0.000354215947482332], [463, 0.00035747943800369073], [464, 0.0003527479721093697], [465, 0.00034790884005034565], [466, 0.0003559643857827784], [467, 0.00035176807668922357], [468, 0.0003487536044375769], [469, 0.00035840600139666926], [470, 0.00035920318241793964], [471, 0.0003422691397985166], [472, 0.00034024383376871667], [473, 0.0003526502075460592], [474, 0.0003417065683474271], [475, 0.00035555245870315865], [476, 0.0003514812512534847], [477, 0.0003498790490925716], [478, 0.000354458857803572], [479, 0.0003626433946839504], [480, 0.00036333102317455493], [481, 0.000366223324652156], [482, 0.00037368769436681165], [483, 0.0003715139846401845], [484, 0.00035958523497759445], [485, 0.00036052404524906587], [486, 0.0003575972819096491], [487, 0.000356923692794276], [488, 0.00034613481993664837], [489, 0.0003353627823959644], [490, 0.00032474872634370147], [491, 0.00033079212321661324], [492, 0.0003167049982070879], [493, 0.0003058201984396773], [494, 0.00029390916840801303], [495, 0.00028183349252212416], [496, 0.00027167791127192213], [497, 0.00026652054410676053], [498, 0.0002577073129202936], [499, 0.0002648922243145366], [500, 0.0002548901828668928], [501, 0.0002524336611792551], [502, 0.00024987626265460656], [503, 0.00025739845412549355], [504, 0.00024946807827439313], [505, 0.0002641649290689702], [506, 0.0002556941119575602], [507, 0.00021147043832881187], [508, 0.0002161036666988966], [509, 0.00029161475847564784], [510, 0.0002981472600810412], [511, 0.00035901604804408426], [512, 0.00036131895185724733], [513, 0.00033252197048480597], [514, 0.0003887272283903984], [515, 0.0003016481161194449], [516, 0.0002884757590262365], [517, 0.000294169323765925], [518, 0.0003013136572670432], [519, 0.0003020548561097353], [520, 0.0002959145336803076], [521, 0.00029668174133616235], [522, 0.00029816360809581263], [523, 0.0002924083144157309], [524, 0.0002864097049714218], [525, 0.00024405688966047705], [526, 0.00023981611313103377], [527, 0.00023216849093821287], [528, 0.0002335792809106317], [529, 0.000269152025867702], [530, 0.0002322551272754732], [531, 0.00023281052391130414], [532, 0.00023131272231205428], [533, 0.00023125985183903533], [534, 0.0002075101788275972], [535, 0.00020805483258806378], [536, 0.00020722697299941219], [537, 0.00020774232306312743], [538, 0.00020954382651594452], [539, 0.00024781133710557454], [540, 0.0002079934221265373], [541, 0.0002082561062536459], [542, 0.00020730393805876827], [543, 0.00020615772552714365], [544, 0.0002029396882125329], [545, 0.00019964316701447378], [546, 0.00019405588836701783], [547, 0.00018963161969614065], [548, 0.00020651779616324056], [549, 0.00020055852082973894], [550, 0.0001945645098949536], [551, 0.00019374697392682331], [552, 0.00017327842012804858], [553, 0.00019332785773484005], [554, 0.00018989511740261707], [555, 0.00018451689148399063], [556, 0.0001609081216870461], [557, 0.00017564418243436048], [558, 0.00017545837592411418], [559, 0.0001736651700856222], [560, 0.0001744042412237492], [561, 0.00017254833114462384], [562, 0.00017154160383431752], [563, 0.0001742065621074224], [564, 0.00018777544973198253], [565, 0.00018662689753575116], [566, 0.0001720118523723205], [567, 0.00017278921401128893], [568, 0.00016945883181003206], [569, 0.00016676003197799676], [570, 0.00017145261690457918], [571, 0.00017206424931563054], [572, 0.00017613571310931257], [573, 0.00017028671629648696], [574, 0.000172171998625147], [575, 0.0002014464300373099], [576, 0.00020431981925788845], [577, 0.00020412740640683087], [578, 0.00021261168672545547], [579, 0.0002138459082860619], [580, 0.00021090793838425092], [581, 0.00020377591162182364], [582, 0.00019994205964271223], [583, 0.0002165189222761923], [584, 0.00019537202206445803], [585, 0.00024640685478452486], [586, 0.00023177673999520064], [587, 0.00023594432156545062], [588, 0.00024384354049641297], [589, 0.00021350841994271103], [590, 0.00022590936597228014], [591, 0.0002086987730738487], [592, 0.0002138138409788955], [593, 0.00024083501122827274], [594, 0.00028272525562611674], [595, 0.00028110286188388504], [596, 0.0002785140778454089], [597, 0.0002775734378537097], [598, 0.0002472572549749177], [599, 0.00023482560489479298], [600, 0.00023289180982828862], [601, 0.00023366134532362966], [602, 0.00019453351519767192], [603, 0.00019182706832392878], [604, 0.00019001802423540838], [605, 0.00018799797914833288], [606, 0.00022183011495842278], [607, 0.0002158222129355574], [608, 0.00021648534538498988], [609, 0.0002006210583612326], [610, 0.00018941934433469506], [611, 0.0001728311475201694], [612, 0.00016942566392262636], [613, 0.00016350414420713243], [614, 0.0001597501645322079], [615, 0.00017451051980987243], [616, 0.00016681145543537902], [617, 0.00016193208035450473], [618, 0.00014796024785753177], [619, 0.0001547702561007567], [620, 0.0001518209899259945], [621, 0.00014850718053529484], [622, 0.00013573433303877322], [623, 0.00013579896804627301], [624, 0.00013251983357886823], [625, 0.00013285827453961844], [626, 0.0001339677608802543], [627, 0.0001532610148917156], [628, 0.00013230916346789983], [629, 0.00015925618952362803], [630, 0.00015904885206320456], [631, 0.00014833604073867271], [632, 0.00014893829518878503], [633, 0.0001462340144055895], [634, 0.0001642654549858032], [635, 0.00018149348854891982], [636, 0.00017340260608914607], [637, 0.00018706840757945636], [638, 0.00019009649125819746], [639, 0.00019471741543546057], [640, 0.00019453201024270255], [641, 0.00019690933399577615], [642, 0.0002022827844419475], [643, 0.00018797974030620998], [644, 0.0001874579400124592], [645, 0.0001718372349257766], [646, 0.00018932295858148214], [647, 0.00016903290924611644], [648, 0.00016650256109657433], [649, 0.0001876585089021243], [650, 0.00018981372709275462], [651, 0.00020751545906146405], [652, 0.00020829319054254612], [653, 0.00020771693266747156], [654, 0.00022731427411772355], [655, 0.0001850864946651515], [656, 0.00018756851687588732], [657, 0.00018780416956685526], [658, 0.00018776963475329906], [659, 0.00020055941014996738], [660, 0.0002050071943803027], [661, 0.00020096119171662065], [662, 0.00021234009293493266], [663, 0.00024080717318160577], [664, 0.0002224872011525835], [665, 0.00022074224765618905], [666, 0.0002186149174724336], [667, 0.00021635964844458506], [668, 0.00021544034210626927], [669, 0.00021328324787385416], [670, 0.0002100092273563395], [671, 0.0002271330703300714], [672, 0.00021193044517343234], [673, 0.0002107718087130197], [674, 0.0002120188240385181], [675, 0.0001557264074156909], [676, 0.00018887450696080708], [677, 0.00020733517578204472], [678, 0.00020749503324505287], [679, 0.00019604209593097644], [680, 0.00019434238719597444], [681, 0.0002023824845275445], [682, 0.00017976387272387675], [683, 0.00018154022202763342], [684, 0.00018483584136595168], [685, 0.00020192914929544336], [686, 0.00023022713664451502], [687, 0.00024186701712433775], [688, 0.00024334607966011168], [689, 0.0002489777093335084], [690, 0.00023966391015045507], [691, 0.00023483791306752505], [692, 0.00023296308231391842], [693, 0.00023318602149288324], [694, 0.00018152485350099603], [695, 0.00017655006690617793], [696, 0.00017358901240752567], [697, 0.00016774076927607683], [698, 0.00016303186545696407], [699, 0.00015684528952155446], [700, 0.0001550495781304359], [701, 0.00016708454235704788], [702, 0.00018270886366537304], [703, 0.00018764650712000517], [704, 0.00021703667774963903], [705, 0.00019572813637691624], [706, 0.0001937589868585413], [707, 0.0001937172089614121], [708, 0.0001828469198029348], [709, 0.00018078521351785125], [710, 0.0001812122598940308], [711, 0.00016592433434599324], [712, 0.00016353463887636884], [713, 0.00014852093597395624], [714, 0.00015459699027397616], [715, 0.0001511072362220082], [716, 0.00015054748671861605], [717, 0.00013194753790437842], [718, 0.00013387104984191147], [719, 0.0001616257198409838], [720, 0.00016413489162066984], [721, 0.0001687970685557377], [722, 0.0002029620383167051]]

# Create vectors: x = absolute frame, y = density [μm-2]
x_axis = []
y_axis = []

for frame in cell_1151:
    x_axis.append(frame[0])
    y_axis.append(frame[1])

print (x_axis)
print (y_axis)
print (len(x_axis), len(y_axis))


# Smooth the real data with a spline:
s = UnivariateSpline(x=x_axis, y=y_axis, s=1)
xs = x_axis
ys = s(xs)

print (xs)
print (ys)
print (len(xs), len(ys))


# Extend cell's lifetime to 100%:
x_axis_arbitrary = [item * 100 for item in x_axis]
step = (x_axis[-1] - x_axis[0] + 1)
x_axis_arbitrary = list(range(x_axis_arbitrary[0], x_axis_arbitrary[-1], step))
x_axis_arbitrary = [item / 100 for item in x_axis_arbitrary]


# Interpolate / extrapolate cell's density at each percentage point:
y_axis_arbitrary = s(x_axis_arbitrary)
print (x_axis_arbitrary)
print (len(x_axis_arbitrary))
print (y_axis_arbitrary)
print (len(y_axis_arbitrary))
print (type(y_axis_arbitrary))

for item in y_axis_arbitrary:
    print (item)

"""
# Plot the thing:
x_ticks = list(range(1, 101, 1))

plt.plot(x_axis, y_axis, color="orange", label="True datapoints")
plt.plot(x_axis, ys, color="blueviolet", label="Smoothing spline", linewidth=2.0)
plt.ylim(0, 0.001)
plt.legend()
plt.title("Single Cell #1151 <pos8, '17_07_31'> Density over Absolute Time")
plt.xlabel("Frame #")
plt.ylabel("Cell Density [μm-2]")
#plt.savefig("/Volumes/lowegrp/Data/Kristina/MDCK_WT_Pure/Cell_1151_Smoothing.jpeg", bbox_inches="tight")
plt.show()
plt.close()


plt.scatter(x_ticks, y_axis_arbitrary, color="firebrick", label="Extrapolation")
plt.ylim(0, 0.001)
plt.legend()
plt.title("Single Cell #1151 <pos8, '17_07_31'> Density over Absolute Time")
plt.xlabel("Frame #")
plt.ylabel("Cell Density [μm-2]")
#plt.savefig("/Volumes/lowegrp/Data/Kristina/MDCK_WT_Pure/Cell_1151_Smoothing.jpeg", bbox_inches="tight")
plt.show()
plt.close()

"""