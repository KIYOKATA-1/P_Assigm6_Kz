import re #import regular expressions

#Get User Input/Пайдаланушы енгізуін алыңыз:
def get_input():
    string = input("~𝐈𝐧𝐩𝐮𝐭 𝐒𝐭𝐫𝐢𝐧𝐠~")
    sample = input("~𝐈𝐧𝐩𝐮𝐭 𝐒𝐚𝐦𝐩𝐥𝐞~")
    return string, sample

#Create Menu/Мәзір жасау:
def menu(string, sample):
    while True:
        print("\n  ~̳C̳h̳o̳o̳s̳e̳ ̳O̳p̳e̳r̳a̳t̳i̳o̳n̳~̳  ")
        print("【１　~　Ｆｉｎｄ　Ａｌｌ】")
        print("【２　~　Ｓｅａｒｃｈ】")
        print("【３　~　Ｓｐｌｉｔ】")
        print("【４　~　Ｓｕｂ】")
        print(" 5 ~ 🄴🅇🄸🅃 ")

        choice = input("↓↓↓↓↓ 🅸🅽🅿🆄🆃 🆈🅾🆄🆁 🅲🅷🅾🅸🅲🅴 ↓↓↓↓↓")

#Add Functional/Функционалды қосу:

        if choice == '1':
            matches = re.findall(sample, string)
            print("𝙈𝙖𝙩𝙘𝙝𝙚𝙨 𝙁𝙤𝙪𝙣𝙙", matches)

        elif choice == "2":
            matches = re.search(sample, string)
            if matches:
                print("𝗠𝗮𝘁𝗰𝗵𝗲𝘀  𝗙𝗼𝘂𝗻𝗱 𝗔𝘀 𝗜𝗻𝗱𝗲𝘅 ", matches.start())
            else:
                print("【ＥＲＲＯＲ】")

        elif choice == '3':
            parts = re.split(sample, string)
            print(" 𝐏𝐚𝐫𝐭𝐬~ " + parts)

        elif choice == '4':
            sub = input("~𝐈𝐧𝐩𝐮𝐭 𝐑𝐞𝐩𝐥𝐚𝐜𝐞𝐦𝐞𝐧𝐭~")
            replace = re.sub(sample, sub, string)
            print("<𝐑𝐞𝐩𝐥𝐚𝐜𝐞𝐝>", replace)

        elif choice == '5':
            break

        else:
            print("🅸🅽🆅🅰🅻🅸🅳 🆂🆈🅽🆃🅰🆇")


string, sample = get_input()
menu(string, sample)


