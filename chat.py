import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    [r"quit",
     ["Take care! See ya around!", "It was nice talking to you. See you soon!"]],
    [r"learn",
     ["What state do you live in? Type the two-letter abbreviation for your state (i.e. al, ca, ny, dc, etc.)", ]],
    [r"donate",
     ["Awesome! Would you like to contribute funds to a nationwide bail project or a bail fund in a specific "
      "state? \nType 'state' for a state-specific bail fund, or 'nationwide' for a nationwide bail project.", ]],
    [r"state", ["Yay! What state do you live in? \nType the state's full name (i.e. alabama, hawaii, new york, "
                "etc.). \nAlaska, New Jersey, and Washington, D.C. eliminated cash bail for most defendants.", ]],
    [r"nationwide", ["Nice! Would you like to donate to the National Bail Fund Network or The Bail Project? \nRespond "
                     "with 'nbfn' for the first option or 'tbp' for the second option.", ]],
    [r"nbfn", ["The National Bail Fund Network is made up of over sixty community bail and bond funds across the "
               "country. \nThe community bail and bond funds that are part of the Network are dedicated to being an "
               "organizing tool aimed at ending pretrial and immigration detention. \nClick/tap on this link or copy "
               "and paste it into your browser to donate: https://www.communityjusticeexchange.org/nbfn-directory "
               "\nThe National Bail Fund Network also has a separate Emergency Response Fund to organize a mass "
               "release of everyone inside of jails and detention centers to prevent the worsening of the COVID-19 "
               "public health crisis. \nOpen this link or copy and paste the link in your browser to donate: "
               "https://secure.actblue.com/donate/bailfundscovid ", ]],
    [r"tbp", ["The Bail Project, Inc. is an unprecedented effort to combat mass incarceration at the front end of the "
              "system. \nThey pay bail for people in need, reuniting families and restoring the presumption of "
              "innocence. \nOpen the link or copy and paste the link into your browser: "
              "https://secure.givelively.org/donate/the-bail-project", ]],
    [r"alabama", ["For bail funds in Birmingham: https://givebutter.com/NobodyLeftBehindBailFund \nFor bail funds in "
                  "Huntsville: https://www.paypal.me/hsvbailfund \nFor bail funds in Montgomery: "
                  "https://www.mgmbailout.com \nOpen the link or copy and paste the link into your browser.", ]],
    [r"arizona", ["For bail funds in Phoenix: https://rb.gy/1k1ovv \nFor bail funds in "
                  "Tucson: https://secure.actblue.com/donate/tsccbf \nOpen the link or copy and paste the link into "
                  "your browser.", ]],
    [r"arkansas", ["Arkansas Freedom Fund: https://www.arfreedomfund.com \nOpen the link or copy and paste the link "
                   "into your browser.", ]],
    [r"california", ["What region are you donating to: Northern California or Southern California? For the first "
                     "option, type 'norcal', for the second option, type 'socal'.", ]],
    [r"norcal", ["Bay Area Anti-Repression Committee Bail Fund: https://rally.org/ARCbailfund \nOakland's People's "
                 "Breakfast Bail Fund: https://linktr.ee/PBO \nNorCal Resist Activist BAIL & ICE Bond Fund: "
                 "https://actionnetwork.org/fundraising/ncrbailfund/ \nSilicon Valley DSA Bail Fund: "
                 "https://siliconvalleydsa.org/donations/ \nOpen the link or copy and paste the link into your browser.", ]],
    [r"socal", ["Los Angeles Action Bail Fund: https://secure.actblue.com/donate/wp4bl \nOrange County Bail Fund: "
                "https://www.gofundme.com/f/orange-county-bail-fund \nSan Luis Obispo Bail Fund: "
                "https://www.paypal.me/SLOBailFund \nOpen the link or copy and paste the link into your browser.", ]],
    [r"colorado", ["Colorado Freedom Fund: https://fundly.com/coloradofreedom \nColorado Springs Protest Support Fund: "
                   "http://chinookcenter.org/Colorado-springs-protest-support-fund/ \nDenver Black Lives Matter Fund: "
                   "https://www.gofundme.com/f/funds-for-protesters-against-police-brutality \nOpen the link or copy "
                   "and paste the link into your browser.", ]],
    [r"connecticut", ["Connecticut Bail Fund: http://www.ctbailfund.org/donate", ]],
    [r"delaware", ["FNB Bail Fund: https://www.gofundme.com/f/fnbbailfundwilm", ]],
    [r"florida", ["Alachua County Bail Fund: https://actionnetwork.org/fundraising/alachua-county-covid-19-bond-fund "
                  "\nJacksonville Community Action Committee: https://www.gofundme.com/f/CommunitySupportFund "
                  "\n(F)empower Community Bond Fund: https://www.paypal.me/freethemall \nFlorida LGBTQ Freedom Fund: "
                  "https://www.lgbtqfund.org/donate-1 \nCollier County Bail Fund: "
                  "https://www.gofundme.com/f/collier-county-bail-fund \nOrlando Dream Defenders Bail Fund: "
                  "https://www.paypal.me/otownsquadd \nTampa Bay Community Support Fund: "
                  "https://www.gofundme.com/f/tampa-bay-community-support-fund \nOpen the link or copy and paste the "
                  "link into your browser.", ]],
    [r"georgia", ["For bail funds in Atlanta: https://rb.gy/em4fii \nFor bail funds in Athens: "
                  "https://www.aadmovement.org/athens-freedom-fund/ \nOpen the link or copy and paste the link into "
                  "your browser.", ]],
    [r"hawaii", ["Hawaii Community Bail Fund: https://rb.gy/dt4xpy \nOpen the link or copy and paste the link into "
                 "your browser.", ]],
    [r"illinois", ["Champaign County Bailout Coalition: https://champaigncountybailoutcoalition.wordpress.com/donate/ "
                   "\nChicago Community Bond Fund: https://chicagobond.org/donate/ \nWinnebago Bond Project: "
                   "https://www.wincoilbondproject.org/donate \nOpen the link or copy and paste the link into your "
                   "browser.", ]],
    [r"indiana", ["Bloomington Black Lives Matter: https://blm.btown-in.org \nOpen the link or copy and paste the "
                  "link into your browser.", ]],
    [r"iowa", ["Prarielands Freedom Fund: "
               "https://communitybondproject.networkforgood.com/projects/101939-free-our-protesters \nOpen the link "
               "or copy and paste the link into your browser.", ]],
    [r"kansas", ["Black Lives Matter Lawrence Bail Fund: https://www.paypal.me/lawrencebailfund \nWichita Bail Fund: "
                 "https://ictdsa.org/bail-fund \nOpen the link or copy and paste the link into your browser.", ]],
    [r"kentucky", ["Louisville Community Bail Fund: https://www.paypal.me/lawrencebailfund \nLexington Bail Fund: "
                   "https://rb.gy/mi6vhi \nOpen the link or copy and paste the link into your browser.", ]],
    [r"louisiana", ["New Orleans Safety & Freedom Fund: https://donorbox.org/safety-freedom-fund-eoy \nYWCA Greater "
                    "Baton Rouge Community Bail Fund: https://www.ywca-br.org/donate \nOpen the link or copy and "
                    "paste the link into your browser.", ]],
    [r"maryland", ["Baltimore Legal Action Team Bail Fund: "
                   "https://baltimoreactionlegal.networkforgood.com/projects/99878-cells-to-safety-campaign-final "
                   "\nOpen the link or copy and paste the link into your browser.", ]],
    [r"massachusetts", ["Massachusetts Bail Fund: https://www.massbailfund.org/donate.html \nBoston Beyond Bond & "
                        "Legal Defense Fund: https://www.beyondbondboston.org/donate \nOpen the link or copy and "
                        "paste the link into your browser.", ]],
    [r"michigan", ["Michigan Solidarity Bail Fund: https://secure.actblue.com/donate/michigan-solidarity-bail-fund "
                   "\nDetroit Justice Center: https://donorbox.org/support-the-detroit-justice-center-1 \nOpen the "
                   "link or copy and paste the link into your browser.", ]],
    [r"minnesota", ["Minnesota Freedom Fund: https://minnesotafreedomfund.org \nOpen the link or copy and paste the "
                    "link into your browser.", ]],
    [r"mississippi", ["Mississippi Bail Fund Collective: https://secure.actblue.com/donate/ms-bail-fund \nOpen the "
                      "link or copy and paste the link into your browser.", ]],
    [r"missouri", ["Reale Justice Community Bail Fund: https://www.paypal.com/pools/c/8dFiVVyGMN \nKansas City "
                   "Community Bail Fund: https://gkccf.kimbia.com/kans61 \nOne Struggle KC Legal Fund: "
                   "https://actionnetwork.org/fundraising/donate-to-the-one-struggle-kc-legal-fund \nOpen the link or "
                   "copy and paste the link into your browser.", ]],
    [r"nebraska", ["Neighbors for Common Good Bail Fund: https://www.paypal.me/neleftcoalition \nOpen the "
                   "link or copy and paste the link into your browser.", ]],
    [r"nevada", ["Vegas Freedom Fund: https://secure.actblue.com/donate/vegasfreedomfund \nOpen the link or copy and "
                 "paste the link into your browser.", ]],
    [r"new jersey", ["New Jersey does not allow for cash bail. \nHowever, open this link or copy and "
                     "paste this link into your browser to learn more about immigration bonds: "
                     "https://www.actionbail.com \nDisclaimer: This organization is not a nonprofit.", ]],
    [r"new mexico", ["Albuquerque Center for Peace & Justice Bail Fund: "
                     "https://abqpeaceandjustice.org/index.php/donate \nOpen the link or copy and paste the link into "
                     "your browser.", ]],
    [r"new york", ["Action Bail Fund NYC: https://afgj.salsalabs.org/actionbailfund/index.html \nAlbany Safety Fund "
                   "For Black Lives: https://www.paypal.com/pools/c/8pAK2AzvDg \nBuffalo Legal, Bail, and Organizing "
                   "Fund: https://fundrazr.com/d1fhz6?ref=ab_0aZkntzNGkQ0aZkntzNGkQ \nOpen the link or copy and paste "
                   "the link into your browser.", ]],
    [r"north carolina", ["Freedom Fighter Bond Fund: https://emancipatenc.org/freedom-fighter-bond-fund/ "
                         "\nCharlotte Uprising: https://cash.app/$WereStillHere \nNorth Carolina Community Bail Fund "
                         "of Durham: https://www.nccbailfund.org \nThe Anti-Racist Activist Fund: "
                         "https://www.takeactionch.com/donations \nForsyth County Community Bail Fund: "
                         "https://forsythcountycbf.org \nOpen the link or copy and paste the link into your "
                         "browser.", ]],
    [r"north dakota", ["Fargo Moorhead Mutual Aid: https://www.paypal.com/pools/c/8oLGbaaeqf \nOpen the link or copy "
                       "and paste the link into your browser.", ]],
    [r"ohio", ["Canton & Akron Bail Fund: https://www.paypal.com/pools/c/8pz5hovrmY \nBLM Cleveland: "
               "https://www.paypal.me/blmcle \nColumbus Freedom Fund: https://www.paypal.me/columbusfreedomfund "
               "\nBeloved Community Church Bail Fund: https://www.givelify.com/givenow/1.0/NTU5MjE=/selection"
               "\nYoungstown Freedom Fund: https://www.paypal.me/youngstownfreedomfun \nOpen the link or copy and "
               "paste the link into your browser.", ]],
    [r"oklahoma", ["Tulsa Black Lives Matter: https://www.paypal.me/BLMOKC \nOpen the link or copy and paste the link "
                   "into your browser.", ]],
    [r"oregon", ["PDX Protest Bail Fund: https://www.gofundme.com/f/pdx-protest-bail-fund \nPortland Freedom Fund: "
                 "https://portlandfreedomfund.org \nOpen the link or copy and paste the link into your browser.", ]],
    [r"pennsylvania", ["Dauphin County Bail Fund: https://dauphincountybailfund.org/donate/ \nBlack Lives Matter Bail "
                       "Fund Lancaster: https://www.gofundme.com/f/lancaster-bail-fund \nPhiladelphia Community Bail "
                       "Fund: https://www.phillybailout.com \nPhiladelphia Bail Fund (certified non-profit, aiming to "
                       "end cash bail in Philadelphia): https://www.phillybailfund.org \nBukit Bail Fund: "
                       "https://www.bukitbailfund.org/donate \nOpen the link or copy and paste the link into "
                       "your browser.", ]],
    [r"rhode island", ["FANG Community Bail Fund: https://www.gofundme.com/f/fangbailfund \nOpen the link or copy and "
                       "paste the link into your browser.", ]],
    [r"south carolina", ["Soda City Bail Fund: https://sodacitybail.org \nBlack Lives Matter Charleston Bail Fund: "
                         "https://www.paypal.me/chsrebellion2020 \nBlack Lives Matter Greenville Bail Fund: "
                         "https://cash.app/$UpstateBLM \nOpen the link or copy and paste the link into your "
                         "browser.", ]],
    [r"tennessee", ["Hamilton County Community Bail Fund: https://www.calebcha.org/bailfund.html \nEnd Money Bail "
                    "Knoxville Bail Fund: https://venmo.com/EndMoneyBail-Knoxville \nMemphis Community Bail Fund: "
                    "https://justcity.org/what-we-do/mcbfund/ \nMid-South Peace BLM Community Bail Fund: "
                    "https://midsouthpeace.org/get-involved/donate-to-support-the-black-lives-matter-community-bail"
                    "-fund/ \nNashville Community Bail Fund: https://nashvillebailfund.org \nOpen the link or copy "
                    "and paste the link into your browser.", ]],
    [r"texas", ["Afiya Dallas Protest Bail Fund: https://www.theafiyacenter.org/afiyabailfund \nLuke 4:18 Bail Fund: "
                "https://faithintx.org/bailfund/ \nEl Paso Fianza Fund: https://www.fianzafund.org/donate.html "
                "\nTarrant County Community Bail Fund: "
                "https://actionnetwork.org/fundraising/tarrant-county-community-bail-fund \nTexas Organizing Project "
                "Bailout Fund: https://secure.everyaction.com/sC7Un4EQkUG-kchkCsFY7Q2 \nHouston Bail Fund: "
                "https://www.houstonbailfund.com \nOpen the link or copy and paste the link into your browser.", ]],
    [r"utah", ["Salt Lake City Community Bail: https://www.gofundme.com/f/c2mvvn-support-protesters-arrested-by-slcpd "
               "\nOpen the link or copy and paste the link into your browser.", ]],
    [r"virginia", ["Richmond Community Bail Fund: https://rvabailfund.org \nRoanoke Community Bail Fund: "
                   "https://chuffed.org/project/rjs-bail-fund \nLynchburg Community Bail Fund (use their Messenger "
                   "bot to donate): https://www.facebook.com/pg/LyhBailFund/about/?ref=page_internal \n757 Solidarity "
                   "Bail Fund: https://tidewatersolidaritycenter.wordpress.com/donate/ \nOpen the link or copy and "
                   "paste the link into your browser.", ]],
    [r"washington", ["Northwest Community Bail Fund: https://www.nwcombailfund.org \nBlack Lives Matter Seattle "
                     "Freedom Fund: https://blacklivesseattle.org/bail-fund/ \nOpen the link or copy and paste the "
                     "link into your browser.", ]],
    [r"west virginia", ["Black Lives Matter West Virginia Bail Fund: https://rb.gy/q8sbsy \nOpen the link or copy and "
                        "paste the link into your browser.", ]],
    [r"wisconsin", ["Free the 350 Bail Fund: https://freethe350bailfund.wordpress.com \nMilwaukee Freedom Fund: "
                    "https://supportwomenshealth.salsalabs.org/mkefreedomfund/index.html \nOpen the link or copy and "
                    "paste the link into your browser.", ]],
    [r"al", ["\nOpen the link or copy and paste the link into your browser.", ]],
]


def chatty():
    print("Welcome to the BailBot!\nPlease type in lowercase English with correct spelling. \nWould you like to donate "
          "or learn more about bail laws in your state? \nType 'donate' to get donation resources or type 'learn' to "
          "get resources about bail laws in your state. \nType 'quit' to exit.")  # default message at the start
    chat = Chat(pairs, reflections)
    chat.converse()


if __name__ == "__main__":
    chatty()
