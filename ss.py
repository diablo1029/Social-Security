import random
from random import randint

sum = 10
while sum > 0:
    sum -= 1
    gender = randint(0,1)
    first_names = [["Abraham","Absalom","Adam","Addison","Adel","Adrian","Albert","Alec","Alfred","Alistair","Alvin","Andrew","Andy","Anthony","Archibald","Archie","Arnold"
,"Arthur","Austen","Barnabe","Bartholomew","Benjamin","Bernard","Bertram","Blake","Bramwell"
,"Caleb","Calvin","Cardew","Carl","Carlton","Chad","Chadwick","Chance","Chase","Chet","Christian","Claude","Clay","Clint","Colby"
,"Colin","Colton","Corey","Corrie","Curtis","Daniel","David","Davy","Delbert","Derek","Dickon","Donald","Douglas","Dwight","Earl","Ebenezer","Edgar"
,"Edmund","Edward","Edwin","Elbert","Elliot","Elmer","Emil","Eric","Ernest","Ethan","Ezekiel","Felix","Floyd","Francis","Frank"
,"Franklin","Frederick","Gabriel","Galton","Gareth","Garth","Geoffrey","George","Gerald","Gerard","Gilbert","Gorden","Gordon","Graham"
,"Grant","Grayson","Hal","Harold","Henry","Herbert","Herman","Hervey","Horace","Hubert","Hudson","Hugh","Humphrey","Hunter","Ian"
,"Jack","Jacob","Jaime","James","Jason","Jasper","Jeb","Jeff","Jeffrey","Jermaine","Jerome","Job","Joey","John","Johnson","Jolyon","Jonas"
,"Jonathan","Joseph","Joshua","Julian","Justin","Keith","Ken","Kenneth","Kevin","Kurt","Lanny","Larry","Laurence","Lawton","Leopold"
,"Lester","Louis","Luther","Malachi","Malcolm","Manuel","Marcus","Mark","Marshall","Martin","Marvin","Matt","Matthew","Maurice","Maximilian"
,"Melvin","Michael","Miles","Milo","Murray","Myron","Nate","Nathan","Neil","Nicholas","Nicolas","Noel","Norman","Nowell","Osbert"
,"Oscar","Osric","Oswald","Otto","Owen","Palmer","Patrick","Paul","Peleg","Peter","Philip","Phillipps","Quentin","Raife","Ralph"
,"Randall","Raymond","Reginald","Reuben","Rex","Richard","Ricky","Robert","Roderick","Rodger","Rodney","Roger","Rogers","Ronald"
,"Rowland","Rufus","Rupert","Russell","Samuel","Sebastian","Shayne","Sigmund","Simon","Stanley","Stephen","Sylvester","Tate","Terence"
,"Thaddeus","Thomas","Timothy","Tobias","Toby","Tony","Travis","Tristan","Valentine","Victor","Vincent","Vivian","Wadsworth","Waldo","Walter"
,"Wayne","Whitney","Wilfred","William","Winston","Xavier"]
, 

["Abigail","Ada","Addys","Adelaide","Adele","Agatha","Agnes","Alaina","Alanna","Alberta","Albina","Alice","Alison","Alma"
,"Alvina","Amanda","Amber","Amelia","Amy","Ana","Andrea","Angel","Angela","Anna","Annabelle","Anne","Annie","Antonia","Arabella"
,"Arda","Aubrey","Audrey","Autumn","Averil","Avis","Aviva","Barbara","Beatrice","Becki","Belinda","Bella","Berenice","Bertha","Betsy","Betty"
,"Blanche","Brenda","Bridget","Bronwen","Bronwyn","Cadence","Candy","Carlene","Carmelita","Carole","Caroline","Carolyn","Cassandra","Cathleen","Cathy"
,"Cecilia","Cecily","Celestia","Celia","Celinda","Charis","Charisse","Charity","Charlotte","Charmaine","Chelsea","Cherry"
,"Cheryl","Chloe","Christabel","Christina","Christy","Claire","Clara","Claribel","Clarissa","Claudia","Clementine","Cleo","Colette"
,"Colleen","Cordelia","Crystal","Cynthia","Daisy","Danielle","Danna","Daphne","Davina"
,"Dawn","Deanna","Deanne","Deborah","Dede","Delia","Denise","Destiny","Diana","Dora","Doreen","Dorothy","Drusilla","Dulcie"
,"Edith","Edna","Edwina","Effie","Eileen","Eleanor","Elektra","Elizabeth","Ella","Ellen","Emily","Emma","Enid","Erika","Estelle","Esther"
,"Esty","Ethel","Ethelreda","Eudora","Eunice","Eva","Eve","Faith","Felicity","Fleur","Flora","Florence","Galenka","Gaynor"
,"Gemma","Genevieve","Georgia","Georgiana","Gertie","Gertrude","Gia","Giselle","Glenda","Grace","Gwen","Gwenda","Gwendolen"
,"Gwendoline","Gwendolyn","Gwyneth","Hannah","Harper","Harriet","Heather","Heidi","Helen","Helena","Helene","Henrietta","Hero","Hester"
,"Hilda","Hodierna","Holly","Honor","Hope","Ida","Imelda","Imogen","Iona","Irene","Iris","Isabella","Isla","Ivy"
,"Jacqueline","Jacqui","Jaime","Jana","Jane","Janie","Jemima","Jemma","Jenna","Jennifer","Jessica","Jessie","Joan","Joanna","Joanne"
,"Joelle","Jolie","Josephine","Joy","Judith","Julianne","June","Karen","Karina","Kathleen","Kathy","Katie","Kaylee"
,"Kelsey","Kierra","Kim","Kirsten","Kristi","Kristin","Lana","Lara","Laura","Lauren","Lauretta","Leah","Leanne","Leila","Leisha"
,"Lena","Lenna","Leonora","Lettice","Liana","Lila","Lilla","Lillian","Lily","Linda","Lois","Lorelei","Loretta","Lorna","Lorraine","Louella","Louisa"
,"Louise","Lucia","Lucinda","Lucy","Lynnette","Mabel","Madge","Maggie","Marcia","Marcie","Margaret","Maria","Mariah","Marian"
,"Marianne","Marie","Marilyn","Marina","Marissa","Marjorie","Marsha","Marta","Mary","Matilda","Maud","Maude","Maureen","Mavis"
,"May","Maya","Medea","Megan","Mehitable","Melanie","Melissa","Mercedes","Michele","Michelle","Millicent","Minna","Miranda","Moira"
,"Myra","Myrna","Myrtle","Nadine","Naila","Nancy","Narcissa","Natalie","Nicola","Nicole","Nina","Nora","Odette","Olivia","Opal"
,"Patience","Patrice","Patsy","Patty","Paula","Paulina","Pearl","Penelope","Penny","Persis","Petunia","Philippa","Poppy","Precious"
,"Priscilla","Rachel","Reba","Rhiannon","Rhoda","Rhonda","Rita","Roberta"
,"Rosamund","Rose","Rosemary","Ruth","Sabrina","Samantha","Sandra","Sarah","Satyana","Selma","Shania","Shannon","Shayla","Sheryl"
,"Sibyl","Sophia","Sophie","Stella","Summer","Susan","Susanna","Susanne","Suzanne","Sylvia","Talitha","Tallulah","Tamara","Tammy","Tara"
,"Teresa","Thelma","Thomasina","Thurza","Tiffany","Tina","Tracy","Trisha","Valerie","Vanessa","Venetia","Vera","Veronica","Victoria"
,"Vilma","Viola","Virginia","Vivian","Wanda","Wendy","Whitney","Wilma","Winifred","Yasmin","Yvette","Yvonne","Zelda"]]
    f_name = random.choice(first_names[gender])
    middle_init = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    m_init = random.choice(middle_init)
    last_names = ["Aaron","Aarons","Abbey","Abbot","Abbott","Acheson","Ackroyd","Adcock","Adelson","Adin"
,"Adkins","Adlam","Adshead","Afford","Aikin","Ainslie","Aitch","Aitchison","Akehurst"
,"Akroyd","Alabaster","Alderdice","Alderman","Alexander","Allard","Allison","Allitt","Allred","Allum"
,"Almond","Altman","Ambler","Amory","Anderson","Anstead","Anstey","Applegate","Appleyard"
,"Arbour","Archer","Armfield","Armistead","Armitstead","Armstead","Armstrong","Arnold"
,"Arthur","Asbridge","Ashbee","Ashby","Ashdown","Assheton","Astle","Astley","Atkin"
,"Atkins","Atkinson","Atlee","Auger","Austen","Auster","Austin","Axford","Axon","Axtell"
,"Axton","Aykroyd","Aylesworth","Ayres","Ayrton","Babbage","Babbs","Badley","Bagshaw"
,"Baily","Bain","Baines","Baker","Ball","Bancroft","Barber","Barker","Barkley","Barleycorn"
,"Barnbrook","Barnet","Barnett","Barry","Bartholomew","Bartlett","Basford","Baskerville"
,"Bassham","Batchelor","Bates","Batton","Bawden","Baxendale","Baxter","Bayer","Bayfield","Bayles"
,"Baynton","Bayntun","Beacham","Beadon","Beal","Beale","Beamont","Beanland","Beard"
,"Beardsley","Beasant","Beaton","Beavers","Beck","Bedford","Bedingfeld","Bedser","Beeby"
,"Beeching","Beer","Beevers","Begley","Bell","Bence","Benedict","Bennett","Bentley","Benton"
,"Berenson","Berkeley","Berker","Berry","Best","Bethell","Bethune","Beyers","Bidder","Biggins"
,"Biggs","Billman","Bingley","Bird","Birdsong","Birtwistle","Bishop","Black","Blackett"
,"Blackman","Blackmon","Blair","Blake","Blalock","Blight","Blinkhorn","Bloodworth"
,"Bloomer","Bloomfield","Blyth","Blythe","Bomford","Bonniwell","Boot","Boothby","Bott"
,"Botterill","Bottomley","Bottrill","Boulding","Boulting","Bowers","Bowes","Bowie","Bowyer"
,"Brabin","Braceful","Bracey","Brack","Brackenridge","Brackman","Bradley","Bragg"
,"Brailsford","Braithwaite","Bramble","Brandis","Braxton","Brayton","Brazier","Breckenridge"
,"Brennan","Brewer","Brewster","Brickman","Bridgewater","Brimson","Brinkley","Broadbridge","Bromfield","Bromley"
,"Brooks","Broom","Broomfield","Broomhall","Brown","Bruce","Bubb","Buckler","Buckley"
,"Bugden","Bull","Burbridge","Burdon","Burgess","Burke","Burks","Burney","Burnham"
,"Burns","Bush","Butcher","Butter","Butters","Byers","Byrd","Bywater","Cadman","Caferro"
,"Camden","Campion","Cantrell","Cantrill","Cantwell","Caple","Carder","Carleton","Carmichael"
,"Carnell","Carpender","Carpenter","Carrell","Carrington","Cartridge","Cartwright"
,"Case","Casely","Catchpole","Caton","Cauley","Cawley","Chalmers","Chamberlain","Chandler"
,"Chapman","Chappell","Chaucer","Cheatham","Checchia","Cheeseman","Cheesman"
,"Cherrill","Childers","Chisenhall","Chisholm","Christie","Clapham","Clapton","Clark"
,"Clarkson","Cleland","Clerk","Cleveland","Cleverley","Cleverly","Clibburn","Cliburn"
,"Clitheroe","Clopton","Cloud","Clowney","Coates","Coats","Cobham","Coburn","Cockerell"
,"Cockerill","Coffin","Cok","Coldwell","Colegrove","Collingwood","Collins","Colvin"
,"Conlee","Conly","Constable","Cook","Cooke","Coombes","Cooper","Copeland","Copleston"
,"Coppersmith","Coppinger","Coppock","Corbin","Corrie","Cortright","Cosgrove","Cotman"
,"Cotton","Coull","Cowell","Cowman","Cox","Cracroft","Crawford","Creelman","Crerar"
,"Crier","Crittenden","Crockett","Crosbie","Crosby","Crossan","Crowley","Cruddas","Cruise"
,"Cruse","Crutcher","Culver","Culverhouse","Cumberbatch","Curren","Currie","Curthoys"
,"Curzon","Cushing","Dallinger","Dalman","Dane","Daneman","Danson","Darwin","Dashwood"
,"Davenport","Davidson","Daw","Dawkins","Dawson","Dean","Dearborn","Deeks","Deller"
,"Derwin","Devall","Devoe","Dewell","Dewing","Dicks","Dilley","Dimbleby","Dingley"
,"Dinning","Dinsmore","Diprose","Dixon","Dobb","Dobbs","Dobson","Dodwell","Donaldson"
,"Donelan","Donovan","Douch","Dowd","Dowdall","Dowden","Dowdeswell","Dowding","Downer"
,"Downing","Dowson","Drake","Drinkwater","Driver","Duckworth","Duddridge","Duke","Dunham"
,"Dunn","Durbridge","Dyal","Eady","Eagle","Eagleman","Eagleton","Eakin","Eakins","Eastwood"
,"Eaton","Ebanks","Eddy","Edwardes","Edwards","Edwin","Egerton","Eggington","Egginton"
,"Eidson","Elwes","Emerson","England","Englefield","Engleman","Entwistle","Evelyn"
,"Every","Fairchild","Faithfull","Falconer","Farlow","Faulkner","Feetham","Ferguson","Finch"
,"Finn","Firby","Firestone","Fitzsimons","Flatley","Fleck","Fleetwood","Fleming","Fletcher","Foat"
,"Forrest","Forster","Fowler","Fox","Frampton","Franks","Freckelton","French","Frith","Frobisher"
,"Froud","Fuller","Galbraith","Gardiner","Gates","Gathercole","Gawley","Gay","Gayfer"
,"Geddes","Genge","Georgeson","Gibbs","Gibson","Giffen","Gilbert","Gilchrist","Gillick"
,"Ginger","Glavin","Glenister","Glover","Godfrey","Gofton","Goggin","Gold","Goldsmith"
,"Goodfriend","Goodheart","Gooding","Goodman","Goodsell","Goodson","Goodwin","Goodwine"
,"Goodwyn","Goring","Gotts","Gould","Gowler","Graeme","Graham","Grainger","Granger","Graves"
,"Greathouse","Greaves","Green","Greenal","Greenbury","Greene","Greengard","Greening"
,"Greenwood","Gregg","Greig","Grist","Groves","Gundy","Gunn","Gunton","Gusfield","Guthrie"
,"Gwatkin","Hackett","Hackman","Hadfield","Hadley","Haigh","Haines","Haldeman","Haley"
,"Hall","Halley","Hallissey","Hallman","Halsey","Ham","Hamerton","Hamill","Hammerton"
,"Hammond","Hampson","Hancock","Hanson","Hardcastle","Harder","Hardstaff","Hardwick"
,"Hardwicke","Hardy","Harenc","Harker","Harman","Harmon","Harold","Harp","Harrelson"
,"Harrold","Hart","Hartnell","Hartnoll","Harvie","Haseltine","Haslem","Hassell","Hastings","Hatfield"
,"Hatton","Hawke","Hawker","Hawkes","Hawking","Hawkins","Hawks","Hawksley","Hawkyard"
,"Hawthorne","Hayden","Hayes","Haylen","Haythornthwaite","Hayward","Haywood","Hazell"
,"Headley","Hearnshaw","Heathcoat","Heathfield","Hebb","Hector","Henson","Hepburn"
,"Heron","Herring","Hervey","Heseltine","Heselton","Heston","Hewlett","Hewson","Heywood"
,"Hicks","Higginbotham","Higgins","Higham","Hill","Hitchcock","Hitchens","Hixon","Hixson"
,"Hodgkinson","Hodgson","Hodierna","Hoffman","Hogan","Holborn","Holder","Holdsworth"
,"Holiday","Holland","Holliday","Honeyball","Hood","Hoover","Hopkins","Hopkinson","Horler"
,"Hornby","Horner","Horniman","Hornsby","Houseman","Hovenden","Howard","Howell","Hubbard"
,"Huckabee","Hudson","Humphrey","Hunt","Hunter","Huntsman","Hustler","Huxley","Huxtable"
,"Hyland","Ingersoll","Inglis","Ingram","Ireton","Irwin","Isler","Jacklin","Jackson"
,"Jacobs","Jacobson","Jeffress","Jennings","Jent","Jepson","Jessop","Jetton","Jewell"
,"Johnson","Johnston","Jolley","Jonas","Jones","Joplin","Jordison","Joseph","Jowett"
,"Kane","Keith","Kelly","Kent","Kenyon","Kersey","Kershaw","Kettle","Keysor","Kinchen"
,"King","Kington","Kirkland","Kitchen","Kitching","Kitt","Kitts","Knaggs","Knott","Kraabel"
,"Kyle","Lainson","Lake","Lamble","Lamp","Lampkin","Laine","Lane","Layne","Fox","Lang"
,"Langford","Langton","Lapthorne","Lard","Laslett","Laughton","Launchbury","Law","Lawrenson"
,"Laws","Lawson","Lawton","Lawyer","Leatherbarrow","Leavitt","Leighton","Lemer","Lennon"
,"Levett","Levick","Levingston","Levinson","Lewis","Light","Lillard","Lillywhite","Lincecum"
,"Lind","Lineker","Linnell","Linwood","Lister","Liston","Little","Livingston","Lloyd"
,"Loates","Lock","Locke","Lolley","Longfield","Longstreet","Love","Lovejoy","Lovell"
,"Lovett","Loving","Lowe","Lucey","Luckinbill","Lucy","Lukis","Lusher","MacAndrew"
,"MacAskill","Macaulay","MacAuley","MacAuliffe","MacCauley","MacCawley","MacCloud"
,"MacFarlane","Mackall","Mackenzie","MacLachlan","MacTavish","Maddux","Maidment","Malgham"
,"Malghum","Manning","Marchbank","Marris","Marsden","Marsh","Marshall","Martin","Mason"
,"Massey","Matterson","Mattingly","Maxwell","May","Mayberry","Mayor","McAuley","McCann"
,"McCauley","McCawley","McCloud","McClure","McGlothlin","McKenna","McKeown","McLennan"
,"McLoud","McMillan","McSorley","Meadows","Melton","Mendenhall","Merchant","Meriweather"
,"Meriwether","Merriman","Merrington","Merritt","Michaelson","Midwinter","Miller"
,"Milnes","Minhinnick","Misselbrook","Mitchell","Mollison","Monk","Monroe","Moore"
,"Morris","Morrison","Morton","Moultrie","Muggeridge","Mullen","Murgatroyd","Mursell"
,"Myers","Myquran","Nance","Nash","Nathan","Natt","Nelson","Nettlefold","Nettles"
,"New","Newbold","Newdigate","Newey","Newhouse","Niccol","Nicholl","Nicholls","Nickson"
,"Nicol","Nicolson","Nightingale","Nihill","Nixon","Noakes","Nolan","Norrington","Norris"
,"Northcutt","Northmore","Nuttall","O'Cawley","O'Dell","O'Leary","O'Reilly","Oatway","Odell","O'Hagan"
,"Orlebar","Orpen","Orr","Orton","Osborne","Ottley","Ousey","Overstreet","Oxley","Padden"
,"Padfield","Page","Paget","Palfrey","Palmer","Palmerston","Pancake","Pankey","Pappin"
,"Parker","Parkes","Parnell","Parrot","Parrott","Patrick","Paulson","Pemberton","Pendelton"
,"Penfold","Perch","Pertwee","Peters","Peterson","Pettit","Pettitt","Peverett","Phelps"
,"Phipps","Phipson","Phoenix","Pickavance","Pickett","Pidgeon","Pierce","Piper","Pippen"
,"Piston","Plumb","Plunkett","Podmore","Poe","Poland","Pollock","Pontifex"
,"Ponting","Porter","Postlethwaite","Postlewait","Potter","Powers","Priest","Provisor","Purdon"
,"Purves","Pynchon","Qualls","Quantrill","Quarrie","Quealy","Quelch","Quigley","Quill"
,"Quimby","Quinnett","Randall","Randel","Randolph","Rateliff","Ratliff","Ravenscroft","Ravenshaw"
,"Rawling","Rawlings","Rayner","Reader","Reading","Reckord","Record","Rector","Redding","Redish"
,"Reeder","Reiner","Renshaw","Reston","Richard","Richards","Richardson","Richmond","Roberts"
,"Robertshaw","Robertson","Robinson","Robson","Rodham","Rose","Roth","Round","Rouse","Rowan","Rowell"
,"Rudner","Runcie","Rundle","Russell","Ryan","Ryeland","Salem","Salmon","Salmons","Sammon"
,"Sammons","Sanders","Sappleton","Sarchet","Saxon","Scriver","Scruton","Seacole","Seals"
,"Seedsman","Sergeant","Seymour","Shairp","Shalders","Shapcott","Sharp","Sharpe","Sharrock"
,"Shave","Shawcross","Shepherd","Sheridan","Sherman","Sherwood","Shipston","Shipway"
,"Shoemaker","Shorrock","Short","Shovelton","Shown","Shurtleff","Shuttleworth","Sibley"
,"Sidney","Simm","Simon","Simons","Simpson","Simson","Sinclair","Skeete","Skillern"
,"Skilling","Skillings","Skippon","Slocumb","Slowey","Smith","Smithers","Smithies"
,"Smithson","Snowden","Sorey","Sorley","Souttar","Spackman","Spain","Sparrow","Speakes"
,"Spencer","Spicer","Spickernell","Spiering","Spooner","Spratt","Springfield","Squire","Squires"
,"Stackhouse","Stanbury","Standing","Stanfield","Stanley","Stansfield","Stanton","Starkey","Staunton"
,"Stephens","Stephenson","Stern","Stetson","Stevens","Stevenson","Stobart","Stone","Stonehouse"
,"Stookey","Strefling","Stuart","Stuckey","Sturgeon","Sugrue","Summerfield","Swaine"
,"Swanston","Swanton","Sweeney","Swinburne","Swinton","Tanner","Teagarden","Tebbutt","Thackeray","Thaxton"
,"Thimbleby","Thirdkill","Thomas","Thompson","Thomson","Thorn","Thornhill","Thornton","Thorpe"
,"Thrasher","Thring","Throsby","Thruston","Thwaite","Tidwell","Tidy","Tillard","Tittle"
,"Tollemache","Toner","Tonra","Torney","Townsend","Towry","Tozer","Trafford","Travers"
,"Trevanion","Trevor-","Roper","Treweek","Trollope","Trotman","Trout","Troutman","Trull","Truss"
,"Tubbs","Tucker","Tuckman","Turnbull","Tuson","Tuttle","Tutton","Twelvetrees","Twyman","Tyndale","Tyndall","Tyrwhitt"
,"Ultan","Underhill","Underwood","Updike","Upshaw","Upton","Vachell","Veal","Verey","Vincent"
,"Virgo","Voyle","Voyles","Wadding","Waddington","Wadsworth","Wainwright","Wakeford","Wakeling","Wall","Walle","Wallis","Wallman","Warburton"
,"Ward","Warren","Wasson","Watchorn","Waterhouse","Wathey","Watkin","Watkins","Watkinson","Watling"
,"Watrous","Watson","Watt","Watters","Wattis","Watts","Waugh","Webber","Weeks","Welbourn"
,"Weller","Wellington","Wells","Wellstone","Welsh","Wentworth","Westfield","Westgate","Westmoreland"
,"Weston","Wheatley","Wheeler","Wheelwright","Whibley","Whidden","Whitaker","White","Whiteside"
,"Whitesides","Whiteway","Whitney","Whittaker","Whittemore","Whittington","Whitworth","Whyte","Wilde"
,"Wilk","Wilkie","Willett","Williams","Williamson","Wilshere","Wilson","Wimshurst"
,"Windeatt","Winder","Windley","Winrow","Winslade","Winter","Winterburn","Witherspoon"
,"Witting","Wolfe","Wolfwood","Wood","Woodard","Woodcock","Woodger","Woodson","Woodville"
,"Woolf","Wordsworth","Workman","Worland","Wornum","Worrall","Worrell","Wren-","Lewis"
,"Wright","Yarbrough","Yeager","Yeo","Yonge","Young","Youngman","Yount","Zeal"]
    l_name = random.choice(last_names)
    height = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    hair_color = ["BRO","BLK","BLD","UNK","GRY"]
    eye_color = ["BLU","BRO","HAZ","GRN"]
    DOB_month = randint(1,12)
    DOB_day = randint(1,30)
    DOB_year = randint(1947,2001)
    E_mail = ["aol", "gmail", "yahoo", "hotmail"]
    email_1 = l_name
    email_0 = "."
    email = f_name
    print (f_name+" "+m_init+" "+l_name)
    print (DOB_month,"/",DOB_day,"/",DOB_year, sep = '')
    if gender == 0:
        print ("Sex: M")
    else :
        print ("Sex: F")

    if gender == 0:
        ft = randint(5,6)
        if ft == 5:
            print (height[5],"'-",height[randint(6,11)],'"', sep = '')
        else :
            print (height[6],"'-",randint(0,3),'"', sep = '')
    else :
        print (height[5],"'-",height[randint(0,11)],'"', sep = '')
    if gender == 0:
        lbs = randint(randint(120,140),randint(230,250))
        print (lbs,"lb",sep = '')
    else :
        lbs = randint(randint(100,110),randint(200,220))
        print (lbs,"lb",sep = '')    
    print ("Eyes:",eye_color[randint(0,3)])
    if DOB_year < 1960:
        print ("Hair:",hair_color[randint(0,4)])
    else :
        print ("Hair:",hair_color[randint(0,2)])
    print (email_1,email_0,email,randint(0,999),"@",random.choice(E_mail),".com", "\n", sep = '')
    
    
    
    