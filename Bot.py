import time
from pyrogram import Client, filters


api_id = 1232300
api_hash = 'dce3183d468a7193a7c6518f20af08f5'
bot_token = '1733161004:AAEfs9lu6FwlrEU08wFV7pEKY9L1iQj-P60'


app = Client("pycharm",api_id=api_id , api_hash= api_hash, bot_token=bot_token)

@app.on_message(filters.command(["start"] ,["/"]))
def start(client , message):
    if message.chat.type  == 'private':
        message.reply(f"Sayın {message.from_user.first_name}\nBen Özel Sohbetler İçin Yapılmadım\nGruplara Ekleyip Mesajları Görmem İçin Boş Tag Verirseniz Sizin İçin Grup Üyelerini Etiketleyebilirim\nCreated by 
@magandadestek
@magandaduyur\nTeşekkürler İyi Günler...")

    elif message.chat.type == 'supergroup' or 'group':
        message.reply("Bot Çalışıyor...\nBotu Kullanmak İçin =  @all SAYI METİN \nCreated by @magandadestek
@magandaduyur")

@app.on_message(filters.private)
def ozel_mesaj(client , message):
    app.send_message(message.chat.id,f"Sayın {message.from_user.first_name}\nBen Özel Sohbetler İçin Yapılmadım\nGruplara Ekleyip Mesajları Görmem İçin Boş Tag Verirseniz Sizin İçin Grup Üyelerini Etiketleyebilirim\nCreated by @magandadestek
@magandaduyur\nTeşekkürler İyi Günler...")

@app.on_message(filters.command(['all'],['@']))
def all(client , message):
    if message.text.split()[1].isnumeric():
        uye_sayi = app.get_chat_members_count(message.chat.id)
        metin = ""
        sayi = int(message.text.split()[1])
        sayac = 0
        kisiler = app.get_chat_members(message.chat.id)

        if uye_sayi < sayi:
            message.reply("Girdiğiniz Sayı Grup Üye Sayısından Fazla !!")
            pass
        else:
            for i in message.text.split()[2:]:
                metin += i + ' '
            message.reply(f"{sayi} kişi etiketleniyor...\n**Sebep** : {metin}__\n**by** @magandadestek
@magandaduyur")

            for kisi in kisiler:

                if kisi.user.is_bot == False:
                    isim = kisi.user.first_name
                    app.send_message(message.chat.id,f"[{isim}](tg://user?id={kisi.user.id}) {metin}")
                    time.sleep(2)

                    sayac += 1
                    if sayac == sayi:
                        app.send_message(message.chat.id,f'{sayi} Kişi Etiketlendi...\nby @magandadestek
@magandaduyur')
                        break


    else:
        metin = ""
        for i in message.text.split()[1:]:
            metin += i + ' '
        sayi = 50
        sayac = 0
        kisiler = app.get_chat_members(message.chat.id)


        message.reply(f"Kişiler etiketleniyor...\n**Sebep** : {metin}\n**by** __@magandadestek
@magandaduyur")

        for kisi in kisiler:
            if kisi.user.is_bot == False:
                isim = kisi.user.first_name
                app.send_message(message.chat.id, f"[{isim}](tg://user?id={kisi.user.id}) {metin}")
                time.sleep(2)

                sayac += 1
                if sayac == sayi:
                    app.send_message(message.chat.id, f'Kişiler Etiketlendi...\nby @magandadestek
@magandaduyur')
                    break


app.r
