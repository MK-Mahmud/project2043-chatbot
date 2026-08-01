import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "abc_bank_chatbot.settings"
)

django.setup()

from chatbot.models import Intent, KnowledgeBase

KnowledgeBase.objects.all().delete()

print("Old KnowledgeBase deleted.")
# -------------------------
# GREETING
# -------------------------

def add_record(intent_name, en_q, ha_q, en_a, ha_a):

    intent = Intent.objects.get(intent_name=intent_name)

    KnowledgeBase.objects.create(
        intent=intent,
        question_en=en_q,
        question_ha=ha_q,
        answer_en=en_a,
        answer_ha=ha_a
    )
    # ==========================================
# GREETING
# ==========================================

add_record(
    "GREETING",
    "Hello",
    "Sannu",
    "Hello! Welcome to ABC Bank SmartAssist. How may I assist you today?",
    "Sannu! Barka da zuwa ABC Bank SmartAssist. Ta yaya zan taimake ka yau?"
)

add_record(
    "GREETING",
    "Hi",
    "Barka",
    "Hi! I'm ABC Bank SmartAssist. How can I help you today?",
    "Sannu! Ni ne ABC Bank SmartAssist. Ta yaya zan taimake ka yau?"
)

add_record(
    "GREETING",
    "Good morning",
    "Barka da safiya",
    "Good morning! Welcome to ABC Bank.",
    "Barka da safiya! Barka da zuwa ABC Bank."
)

add_record(
    "GREETING",
    "Good afternoon",
    "Barka da rana",
    "Good afternoon! What banking service do you need today?",
    "Barka da rana! Wane irin sabis na banki kake bukata?"
)

add_record(
    "GREETING",
    "Good evening",
    "Barka da yamma",
    "Good evening! I'm here to help with your banking questions.",
    "Barka da yamma! Ina nan domin taimaka maka da tambayoyin banki."
)
# ==========================================
# ACCOUNT_OPENING
# ==========================================

add_record(
    "ACCOUNT_OPENING",
    "I want to open an account",
    "Ina son bude account",
    "You can open a savings or current account by visiting any ABC Bank branch with a valid means of identification, passport photograph, proof of address and your BVN.",
    "Za ka iya bude savings ko current account ta hanyar ziyartar kowane reshen ABC Bank tare da katin shaida, hoton fasfo, shaidar adireshi da BVN."
)

add_record(
    "ACCOUNT_OPENING",
    "How do I open an account?",
    "Yaya zan bude account?",
    "Opening an account is easy. Visit any ABC Bank branch or use our online account opening service.",
    "Bude account abu ne mai sauki. Ziyarci reshen ABC Bank ko amfani da sabis na bude account ta yanar gizo."
)

add_record(
    "ACCOUNT_OPENING",
    "What documents do I need to open an account?",
    "Wadanne takardu ake bukata domin bude account?",
    "You need a valid ID, BVN, passport photograph and proof of address to open an account.",
    "Kana bukatar katin shaida, BVN, hoton fasfo da shaidar adireshi domin bude account."
)

add_record(
    "ACCOUNT_OPENING",
    "Can I open an account online?",
    "Zan iya bude account ta yanar gizo?",
    "Yes. ABC Bank allows customers to begin the account opening process online before visiting a branch for verification if required.",
    "Eh. ABC Bank tana ba da damar fara bude account ta yanar gizo kafin zuwa reshe idan ana bukatar tantancewa."
)

add_record(
    "ACCOUNT_OPENING",
    "I need a new bank account",
    "Ina bukatar sabon account",
    "Our customer service team will guide you through the account opening process and help you choose the most suitable account.",
    "Ma'aikatanmu za su taimaka maka wajen bude account da kuma zabar wanda ya dace da kai."
)
# ==========================================
# LOAN_INQUIRY
# ==========================================

add_record(
    "LOAN_INQUIRY",
    "I need a loan",
    "Ina bukatar rance",
    "ABC Bank offers personal, business and education loans. Visit the nearest branch or apply online to begin your application.",
    "ABC Bank tana bayar da rancen mutum, kasuwanci da ilimi. Ziyarci reshen banki mafi kusa ko yi rajista ta yanar gizo domin fara neman rance."
)

add_record(
    "LOAN_INQUIRY",
    "How can I apply for a loan?",
    "Yaya zan nemi rance?",
    "You can apply for a loan online or visit any ABC Bank branch with the required documents.",
    "Za ka iya neman rance ta yanar gizo ko ziyartar kowane reshen ABC Bank tare da takardun da ake bukata."
)

add_record(
    "LOAN_INQUIRY",
    "What documents are required for a loan?",
    "Wadanne takardu ake bukata domin rance?",
    "A valid means of identification, BVN, proof of income and other supporting documents may be required depending on the loan type.",
    "Ana iya bukatar katin shaida, BVN, shaidar samun kudin shiga da sauran takardu gwargwadon nau'in rancen."
)

add_record(
    "LOAN_INQUIRY",
    "How long does loan approval take?",
    "Yaushe ake amincewa da rance?",
    "Loan approval depends on document verification and eligibility assessment. Our staff will keep you informed throughout the process.",
    "Amincewa da rance ya danganta da tantance takardu da cancanta. Ma'aikatanmu za su sanar da kai yadda aikin ke tafiya."
)

add_record(
    "LOAN_INQUIRY",
    "Can I get a business loan?",
    "Zan iya samun rancen kasuwanci?",
    "Yes. ABC Bank provides business loans for eligible customers. Visit a branch to learn about available loan packages.",
    "Eh. ABC Bank tana bayar da rancen kasuwanci ga kwastomomin da suka cancanta. Ziyarci reshen banki domin karin bayani."
)
# ==========================================
# MONEY_TRANSFER
# ==========================================

add_record(
    "MONEY_TRANSFER",
    "I want to transfer money",
    "Ina son tura kudi",
    "You can transfer money using the ABC Bank mobile app, internet banking platform, USSD service, or by visiting any of our branches.",
    "Za ka iya tura kudi ta amfani da manhajar ABC Bank, internet banking, lambar USSD ko ta ziyartar kowane reshen bankinmu."
)

add_record(
    "MONEY_TRANSFER",
    "How do I transfer money?",
    "Yaya zan tura kudi?",
    "Log in to the ABC Bank mobile app or internet banking, select 'Transfer', enter the beneficiary's details, and confirm the transaction.",
    "Shiga cikin manhajar ABC Bank ko internet banking, zaɓi 'Transfer', saka bayanan wanda za a tura wa kuɗin sannan ka tabbatar da cinikin."
)

add_record(
    "MONEY_TRANSFER",
    "Can I transfer money to another bank?",
    "Zan iya tura kudi zuwa wani banki?",
    "Yes. ABC Bank allows transfers to both ABC Bank accounts and accounts in other banks across Nigeria.",
    "Eh. ABC Bank tana ba da damar tura kuɗi zuwa account na ABC Bank da kuma sauran bankuna a Najeriya."
)

add_record(
    "MONEY_TRANSFER",
    "What are the transfer charges?",
    "Nawa ake biya wajen tura kudi?",
    "Transfer charges depend on the transaction amount and the destination bank. Please refer to our current banking tariff guide for details.",
    "Kudin tura kuɗi ya danganta da adadin kuɗin da bankin da ake turawa. Da fatan za a duba jadawalin kuɗaɗen sabis na bankinmu."
)

add_record(
    "MONEY_TRANSFER",
    "Transfer funds",
    "Tura kudi",
    "ABC Bank provides secure and fast fund transfer services through multiple banking channels.",
    "ABC Bank tana samar da amintaccen kuma saurin sabis na tura kuɗi ta hanyoyin banki daban-daban."
)
# ==========================================
# ACCOUNT_BALANCE
# ==========================================

add_record(
    "ACCOUNT_BALANCE",
    "Check my balance",
    "Duba balance dina",
    "You can check your account balance using the ABC Bank mobile app, internet banking, USSD banking service, ATM, or by visiting any ABC Bank branch.",
    "Za ka iya duba balance dinka ta amfani da manhajar ABC Bank, internet banking, lambar USSD, ATM ko ta ziyartar kowane reshen ABC Bank."
)

add_record(
    "ACCOUNT_BALANCE",
    "What is my account balance?",
    "Nawa ne balance dina?",
    "For security reasons, your account balance can only be viewed after logging into your ABC Bank mobile app, internet banking account, or by using an ATM.",
    "Domin tsaro, za ka iya ganin balance dinka ne kawai bayan shiga cikin manhajar ABC Bank, internet banking ko amfani da ATM."
)

add_record(
    "ACCOUNT_BALANCE",
    "How do I check my account balance?",
    "Yaya zan duba balance dina?",
    "Simply log in to your ABC Bank mobile application or dial the approved USSD banking code to view your current account balance.",
    "Shiga cikin manhajar ABC Bank ko amfani da lambar USSD ta banki domin ganin balance dinka na yanzu."
)

add_record(
    "ACCOUNT_BALANCE",
    "Show me my balance",
    "Nuna min balance dina",
    "ABC Bank provides several secure ways to check your account balance, including Mobile Banking, Internet Banking, ATM, and USSD services.",
    "ABC Bank tana ba da hanyoyi masu aminci domin duba balance, ciki har da Mobile Banking, Internet Banking, ATM da USSD."
)

add_record(
    "ACCOUNT_BALANCE",
    "I want to know my balance",
    "Ina son sanin balance dina",
    "To protect your privacy, your balance is available only after secure authentication through our banking channels.",
    "Domin kare sirrinka, balance dinka yana samuwa ne kawai bayan tantancewa ta hanyoyin bankinmu."
)
# ==========================================
# ATM_PIN_RESET
# ==========================================

add_record(
    "ATM_PIN_RESET",
    "I forgot my ATM PIN",
    "Na manta ATM PIN dina",
    "If you have forgotten your ATM PIN, please visit the nearest ABC Bank branch or use our self-service channels if available to request a PIN reset.",
    "Idan ka manta ATM PIN dinka, ka ziyarci reshen ABC Bank mafi kusa ko amfani da hanyoyinmu na self-service idan suna samuwa domin sake saita PIN."
)

add_record(
    "ATM_PIN_RESET",
    "How do I reset my ATM PIN?",
    "Yaya zan sake saita ATM PIN dina?",
    "You can reset your ATM PIN by visiting any ABC Bank branch or following the ATM PIN reset procedure through our approved banking channels.",
    "Za ka iya sake saita ATM PIN ta ziyartar kowane reshen ABC Bank ko bin hanyar sake saita PIN ta hanyoyin bankinmu."
)

add_record(
    "ATM_PIN_RESET",
    "My ATM PIN is blocked",
    "ATM PIN dina ya kulle",
    "If your ATM PIN has been blocked, please contact ABC Bank Customer Support or visit the nearest branch for assistance.",
    "Idan ATM PIN dinka ya kulle, ka tuntubi sashen kula da kwastomomi na ABC Bank ko ka ziyarci reshen banki mafi kusa."
)

add_record(
    "ATM_PIN_RESET",
    "Can I change my ATM PIN?",
    "Zan iya canza ATM PIN dina?",
    "Yes. You can change your ATM PIN securely at any ABC Bank ATM or by following the approved PIN change process.",
    "Eh. Za ka iya canza ATM PIN dinka cikin aminci a kowanne ATM na ABC Bank ko ta hanyar da banki ya amince da ita."
)

add_record(
    "ATM_PIN_RESET",
    "I need a new ATM PIN",
    "Ina bukatar sabon ATM PIN",
    "Our customer service team will assist you with generating or resetting your ATM PIN after verifying your identity.",
    "Ma'aikatanmu za su taimaka maka wajen samun sabon ATM PIN bayan an tabbatar da shaidarka."
)
# ==========================================
# DEBIT_CARD
# ==========================================

add_record(
    "DEBIT_CARD",
    "I need a debit card",
    "Ina bukatar katin debit",
    "ABC Bank offers secure debit cards that can be used for ATM withdrawals, online payments, and purchases at merchant locations.",
    "ABC Bank tana bayar da katin debit mai tsaro wanda za a iya amfani da shi wajen cire kudi daga ATM, biyan kudi ta yanar gizo da kuma sayayya."
)

add_record(
    "DEBIT_CARD",
    "How do I apply for a debit card?",
    "Yaya zan nemi katin debit?",
    "You can apply for a debit card by visiting any ABC Bank branch with a valid means of identification.",
    "Za ka iya neman katin debit ta ziyartar kowane reshen ABC Bank tare da katin shaida mai inganci."
)

add_record(
    "DEBIT_CARD",
    "My debit card is lost",
    "Na rasa katin debit dina",
    "If your debit card is lost or stolen, immediately block the card through the mobile app or contact ABC Bank Customer Support.",
    "Idan katin debit dinka ya bace ko aka sace shi, toshe katin nan da nan ta manhajar banki ko tuntubi sashen kula da kwastomomi na ABC Bank."
)

add_record(
    "DEBIT_CARD",
    "My debit card has expired",
    "Katin debit dina ya kare",
    "Please visit the nearest ABC Bank branch to request a replacement debit card.",
    "Da fatan za ka ziyarci reshen ABC Bank mafi kusa domin neman sabon katin debit."
)

add_record(
    "DEBIT_CARD",
    "How long does it take to get a debit card?",
    "Yaushe zan samu katin debit?",
    "The time required depends on the branch and card type. Our staff will inform you when your debit card is ready for collection.",
    "Lokacin da ake bukata ya danganta da reshen banki da nau'in katin. Ma'aikatanmu za su sanar da kai lokacin da katin ya shirya."
)
# ==========================================
# INTERNET_BANKING
# ==========================================

add_record(
    "INTERNET_BANKING",
    "I want internet banking",
    "Ina son internet banking",
    "ABC Bank Internet Banking allows you to transfer funds, pay bills, check your account balance, and manage your account securely from anywhere.",
    "Internet Banking na ABC Bank yana ba ka damar tura kudi, biyan kudade, duba balance da gudanar da account dinka cikin aminci daga ko'ina."
)

add_record(
    "INTERNET_BANKING",
    "How do I register for internet banking?",
    "Yaya zan yi rajistar internet banking?",
    "You can register for Internet Banking by visiting any ABC Bank branch or through our official website if online registration is available.",
    "Za ka iya yin rajistar Internet Banking ta ziyartar reshen ABC Bank ko ta gidan yanar gizonmu idan akwai rajistar ta yanar gizo."
)

add_record(
    "INTERNET_BANKING",
    "I forgot my internet banking password",
    "Na manta kalmar sirrin internet banking dina",
    "If you forgot your Internet Banking password, use the 'Forgot Password' option or contact ABC Bank Customer Support for assistance.",
    "Idan ka manta kalmar sirrin Internet Banking, yi amfani da zabin 'Forgot Password' ko tuntubi sashen kula da kwastomomi na ABC Bank."
)

add_record(
    "INTERNET_BANKING",
    "Is internet banking secure?",
    "Internet banking yana da tsaro?",
    "Yes. ABC Bank Internet Banking uses advanced security measures to protect your personal and financial information.",
    "Eh. Internet Banking na ABC Bank yana amfani da manyan matakan tsaro domin kare bayananka da kudinka."
)

add_record(
    "INTERNET_BANKING",
    "What can I do with internet banking?",
    "Me zan iya yi da internet banking?",
    "With ABC Bank Internet Banking you can transfer money, pay bills, check balances, download statements, and manage your account online.",
    "Da Internet Banking na ABC Bank za ka iya tura kudi, biyan kudade, duba balance, sauke bank statement da kuma kula da account dinka ta yanar gizo."
)
# ==========================================
# MOBILE_BANKING
# ==========================================

add_record(
    "MOBILE_BANKING",
    "I want mobile banking",
    "Ina son mobile banking",
    "ABC Bank Mobile Banking allows you to transfer funds, pay bills, buy airtime, check your account balance, and manage your account from your smartphone.",
    "Manhajar Mobile Banking ta ABC Bank tana ba ka damar tura kudi, biyan kudade, sayen kati, duba balance da kuma kula da account dinka ta wayar hannu."
)

add_record(
    "MOBILE_BANKING",
    "How do I register for mobile banking?",
    "Yaya zan yi rajistar mobile banking?",
    "Download the ABC Bank Mobile App from the Google Play Store or Apple App Store and follow the registration instructions.",
    "Sauke manhajar ABC Bank daga Google Play Store ko Apple App Store sannan ka bi umarnin rajista."
)

add_record(
    "MOBILE_BANKING",
    "I forgot my mobile banking password",
    "Na manta kalmar sirrin mobile banking dina",
    "If you forgot your Mobile Banking password, use the 'Forgot Password' option within the app or contact ABC Bank Customer Support.",
    "Idan ka manta kalmar sirrin Mobile Banking, yi amfani da zabin 'Forgot Password' cikin manhajar ko tuntubi sashen kula da kwastomomi na ABC Bank."
)

add_record(
    "MOBILE_BANKING",
    "What can I do with mobile banking?",
    "Me zan iya yi da mobile banking?",
    "ABC Bank Mobile Banking enables you to transfer money, pay bills, purchase airtime, check balances, view transaction history, and manage your account securely.",
    "Mobile Banking na ABC Bank yana ba ka damar tura kudi, biyan kudade, sayen kati, duba balance, ganin tarihin ciniki da kuma kula da account dinka cikin aminci."
)

add_record(
    "MOBILE_BANKING",
    "Is mobile banking safe?",
    "Mobile banking yana da tsaro?",
    "Yes. ABC Bank Mobile Banking uses secure authentication and encryption technologies to protect your banking information.",
    "Eh. Mobile Banking na ABC Bank yana amfani da hanyoyin tsaro da boye bayanai domin kare bayananka da harkokin bankinka."
)
# ==========================================
# BRANCH_LOCATION
# ==========================================

add_record(
    "BRANCH_LOCATION",
    "Where is your nearest branch?",
    "Ina reshen banki mafi kusa?",
    "You can visit any ABC Bank branch nearest to your location. Please use our official website or mobile app to find the closest branch.",
    "Za ka iya ziyartar reshen ABC Bank mafi kusa da kai. Da fatan za ka yi amfani da gidan yanar gizonmu ko manhajar wayar hannu domin gano reshen mafi kusa."
)

add_record(
    "BRANCH_LOCATION",
    "Where is ABC Bank located?",
    "Ina ABC Bank take?",
    "ABC Bank has branches across the country. Please tell me your city or state so I can help you locate the nearest branch.",
    "ABC Bank tana da rassa a fadin kasar nan. Ka fada min jihar ko garin da kake domin in taimaka maka samun reshen mafi kusa."
)

add_record(
    "BRANCH_LOCATION",
    "Find the nearest branch",
    "Nemo min reshen banki mafi kusa",
    "Our branches are available in major cities nationwide. You can also use our mobile app to locate the nearest branch.",
    "Rassanmu suna cikin manyan biranen kasar nan. Hakanan zaka iya amfani da manhajar mu domin gano reshen mafi kusa."
)

add_record(
    "BRANCH_LOCATION",
    "What are your branch opening hours?",
    "Wani lokaci banki yake budewa?",
    "Most ABC Bank branches operate from Monday to Friday between 8:00 AM and 4:00 PM. Some branches may have extended banking hours.",
    "Yawancin rassan ABC Bank suna bude daga Litinin zuwa Juma'a tsakanin karfe 8:00 na safe zuwa 4:00 na yamma. Wasu rassan suna da karin lokacin aiki."
)

add_record(
    "BRANCH_LOCATION",
    "Is there an ABC Bank branch near me?",
    "Akwai reshen ABC Bank kusa da ni?",
    "Please provide your location and I'll help you identify the nearest ABC Bank branch.",
    "Da fatan za ka bayyana inda kake domin in taimaka maka gano reshen ABC Bank mafi kusa."
)
# ==========================================
# CUSTOMER_SUPPORT
# ==========================================

add_record(
    "CUSTOMER_SUPPORT",
    "I need customer support",
    "Ina bukatar taimakon kwastomomi",
    "Our Customer Support team is available to assist you with any banking questions or issues. You can contact us by phone, email, or visit the nearest ABC Bank branch.",
    "Sashen kula da kwastomomi na ABC Bank yana shirye ya taimaka maka da kowace tambaya ko matsalar banki. Za ka iya tuntubar mu ta waya, imel ko ziyartar reshen banki mafi kusa."
)

add_record(
    "CUSTOMER_SUPPORT",
    "How can I contact customer service?",
    "Yaya zan tuntubi sashen kula da kwastomomi?",
    "You can contact ABC Bank Customer Support through our customer care hotline, official email address, or by visiting any branch.",
    "Za ka iya tuntubar sashen kula da kwastomomi na ABC Bank ta layin waya, imel na hukuma, ko ta ziyartar kowane reshen bankinmu."
)

add_record(
    "CUSTOMER_SUPPORT",
    "I have a complaint",
    "Ina da korafi",
    "We are sorry for the inconvenience. Please provide details of your complaint and our Customer Support team will investigate and assist you.",
    "Muna ba da hakuri kan matsalar da ka fuskanta. Da fatan za ka bayyana korafinka domin ma'aikatanmu su bincika su taimaka maka."
)

add_record(
    "CUSTOMER_SUPPORT",
    "I need help",
    "Ina bukatar taimako",
    "I'm here to help. Please tell me what banking service or issue you need assistance with.",
    "Ina nan domin taimaka maka. Da fatan za ka bayyana irin sabis ko matsalar bankin da kake bukatar taimako akai."
)

add_record(
    "CUSTOMER_SUPPORT",
    "Can I speak to an agent?",
    "Zan iya magana da ma'aikaci?",
    "Yes. If you need further assistance, you can speak with one of our Customer Support representatives by visiting any branch or calling our customer care line.",
    "Eh. Idan kana bukatar karin taimako, za ka iya magana da daya daga cikin ma'aikatan kula da kwastomomi ta ziyartar reshen banki ko kiran layin kula da kwastomomi."
)
# ==========================================
# BANK_INFORMATION
# ==========================================

add_record(
    "BANK_INFORMATION",
    "Tell me about ABC Bank",
    "Ka fada min game da ABC Bank",
    "ABC Bank is committed to providing secure, reliable, and innovative banking services to individuals and businesses. We offer savings accounts, current accounts, loans, debit cards, mobile banking, internet banking, and money transfer services.",
    "ABC Bank ta himmatu wajen samar da amintattun kuma ingantattun ayyukan banki ga mutane da kasuwanci. Muna bayar da savings account, current account, rance, katin debit, mobile banking, internet banking da sabis na tura kudi."
)

add_record(
    "BANK_INFORMATION",
    "What services do you offer?",
    "Wadanne ayyuka kuke bayarwa?",
    "ABC Bank offers account opening, loans, debit cards, fund transfers, mobile banking, internet banking, ATM services, and customer support.",
    "ABC Bank tana bayar da bude account, rance, katin debit, tura kudi, mobile banking, internet banking, ayyukan ATM da kuma kula da kwastomomi."
)

add_record(
    "BANK_INFORMATION",
    "What are your banking services?",
    "Menene ayyukan bankinku?",
    "Our banking services include savings and current accounts, personal and business loans, debit cards, mobile banking, internet banking, and secure payment services.",
    "Ayyukan bankinmu sun hada da savings da current account, rancen mutum da kasuwanci, katin debit, mobile banking, internet banking da kuma amintattun hanyoyin biyan kudi."
)

add_record(
    "BANK_INFORMATION",
    "What is ABC Bank?",
    "Menene ABC Bank?",
    "ABC Bank is a modern financial institution dedicated to delivering quality banking solutions with excellent customer service and secure digital banking platforms.",
    "ABC Bank cibiyar hada-hadar kudi ce ta zamani wacce ke samar da ingantattun hanyoyin banki tare da kyakkyawan kulawa ga kwastomomi da kuma amintattun hanyoyin banki na zamani."
)

add_record(
    "BANK_INFORMATION",
    "Can you tell me about your bank?",
    "Za ka iya fada min game da bankinku?",
    "ABC Bank provides convenient banking solutions through our branches, ATMs, Mobile Banking, Internet Banking, and dedicated Customer Support services.",
    "ABC Bank tana samar da saukin ayyukan banki ta rassanmu, ATM, Mobile Banking, Internet Banking da kuma sashen kula da kwastomomi."
)
print("Knowledge Base populated successfully!")
print("=" * 40)
print("Knowledge Base populated successfully!")
print("Total records:", KnowledgeBase.objects.count())
print("=" * 40)