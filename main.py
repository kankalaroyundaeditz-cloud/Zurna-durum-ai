import os
import random
import webbrowser

from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle
from kivy.metrics import dp
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.clock import Clock
from kivy.uix.stencilview import StencilView


# =========================================================
# 📁 DOSYALARIN BULUNDUĞU KLASÖR
# =========================================================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# =========================================================
# 🖼️ YUVARLAK FOTOĞRAF
# =========================================================

class YuvarlakFoto(StencilView):

    def __init__(self, kaynak, **kwargs):
        super().__init__(**kwargs)

        self.size_hint = (None, None)
        self.size = (dp(60), dp(60))

        yol = os.path.join(BASE_DIR, kaynak)

        self.foto = Image(
            source=yol,
            size=self.size,
            allow_stretch=True,
            keep_ratio=False
        )

        self.add_widget(self.foto)

        self.bind(
            pos=self.foto_guncelle,
            size=self.foto_guncelle
        )

    def foto_guncelle(self, *args):
        self.foto.pos = self.pos
        self.foto.size = self.size

    def on_touch_down(self, touch):
        return super().on_touch_down(touch)


# =========================================================
# 💬 MESAJ BALONU
# =========================================================

class MesajBalonu(Label):

    def __init__(self, arka_plan, **kwargs):
        super().__init__(**kwargs)

        self.padding = (15, 10)
        self.size_hint_y = None

        self.bind(
            width=self.yaziyi_sar
        )

        with self.canvas.before:
            Color(*arka_plan)

            self.kutu = RoundedRectangle(
                pos=self.pos,
                size=self.size,
                radius=[dp(15)]
            )

        self.bind(
            pos=self.kutuyu_guncelle,
            size=self.kutuyu_guncelle
        )

        self.bind(
            texture_size=self.yuksekligi_ayarla
        )

    def yaziyi_sar(self, *args):

        self.text_size = (
            self.width - dp(30),
            None
        )

    def kutuyu_guncelle(self, *args):

        self.kutu.pos = self.pos
        self.kutu.size = self.size

    def yuksekligi_ayarla(self, *args):

        self.height = self.texture_size[1] + dp(20)


# =========================================================
# 💬 MESAJ SATIRI
# =========================================================

class MesajSatiri(BoxLayout):

    def __init__(
        self,
        sagda=False,
        avatar="",
        **kwargs
    ):

        super().__init__(**kwargs)

        self.orientation = "horizontal"
        self.size_hint_y = None
        self.height = dp(90)
        self.spacing = dp(8)

        # =============================================
        # 👤 FOTOĞRAF
        # =============================================

        if avatar:

            foto = YuvarlakFoto(avatar)

            if sagda:

                # Senin mesajın:
                # boşluk → balon → fotoğraf

                self.add_widget(Widget())

            self.add_widget(foto)


# =========================================================
# 🌯 ZURNA DÜRÜM AI
# =========================================================

class ZurnaDurumApp(App):

    def build(self):

        # =================================================
        # 🧠 ZURNA DÜRÜM'ÜN BİLGİ TABANI
        # =================================================

        self.bilgi_tabani = {

            "selam": [
                "ne selamı birader, sadede gel açtık! 😎",
                "selam kanka🫡",
                "hoş geldin ahbap🥂"
            ],

            "kimsin": [
                "ben zurna dürüm ai, buraların en profesyonel yapay zekasıyım! 🌯",
                "buralarin en kral, en profesyonel 70 santimlik zurna durumuyum ben!"
            ],

            "hobilerin ne": [
                "benim hobilerim zurna dürüm yiyip ayran içmek! 😎🌯"
            ],

            "2+2": [
                "bana bu kadar kolay soru sorma ahbap 😂"
            ],

            "zurna dürüm biz neredeyiz": [
                "buradayız kanka 😂"
            ],

            "mal": [
                "kime mal diyorsun lan sen?! buralarin en profesyonel durumuyum!",
                "laflarina dikkat et kaptan, yoksa sisteme aci biber sosu sıkarım!"
            ],

            "iki kuzu kulagi": [
                "beyfendi burası zara"
            ],

            "şahadet getir": [
                "eşedü enlâ ilahe illalah ve eşhedü enne muhanmeden abduhu ve rasuluhu"
            ],

            "chatpgt senden daha iyi": [
                "haklısın ama eminimki yakında onu geçicem"
            ],

            "kek nedir": [
                "kek bir yaşam bir aile bir tutku ve bir ilhamdır"
            ],

            "nerelisin": [
                "has çorumluyum heri"
            ],

            "dunyayı ele geçiricek misin?": [
                "dünyayı ele geçirmek mi buna ihtiyacım yokki"
            ],

            "sahibin kim": [
                "o mühteşem kişiler okadar iyi ki tanımlıyamıyorum"
            ],

            "istanbulu kim fet etti": [
                "o tüm her yeri fet etti aslında sadece istanbulu değil bunu bil yeter"
            ],

            "yapay zekalar dünyayı ne zaman ele geçricek çok merak ediyorum": [
                "geri sayımı başlatıyorum bir ikiii üççç dört beşş patlama aktif... puhaha bu bir şakaydı"
            ]
        }

        # =================================================
        # 📱 ANA EKRAN
        # =================================================

        ana_ekran = BoxLayout(
            orientation="vertical",
            padding=20,
            spacing=10
        )

        # =================================================
        # 🌈 HAREKETLİ BAŞLIK
        # =================================================

        self.renkler = [
            "ff0000",
            "ff8800",
            "ffff00",
            "00ff00",
            "00aaff",
            "5500ff",
            "aa00ff",
            "ff00aa"
        ]

        self.renk_offset = 0

        self.baslik = Label(
            text="",
            markup=True,
            font_size=32,
            bold=True,
            size_hint_y=None,
            height=70
        )

        ana_ekran.add_widget(self.baslik)

        self.renkli_basligi_guncelle()

        Clock.schedule_interval(
            self.rainbow_guncelle,
            0.15
        )

        # =================================================
        # 💬 SOHBET ALANI
        # =================================================

        self.sohbet = BoxLayout(
            orientation="vertical",
            spacing=10,
            size_hint_y=None
        )

        self.sohbet.bind(
            minimum_height=self.sohbet.setter("height")
        )

        ana_ekran.add_widget(self.sohbet)

        # =================================================
        # ⌨️ MESAJ KUTUSU
        # =================================================

        self.mesaj_kutusu = TextInput(
            hint_text="Mesajını yaz...",
            multiline=False,
            size_hint_y=None,
            height=70
        )

        ana_ekran.add_widget(
            self.mesaj_kutusu
        )

        # =================================================
        # 🟢 BUTON
        # =================================================

        buton = Button(
            text="DURUMU TETİKLE",
            font_size=20,
            size_hint_y=None,
            height=70,
            background_normal="",
            background_color=(0, 1, 0, 1)
        )

        buton.bind(
            on_press=self.cevap_ver
        )

        ana_ekran.add_widget(
            buton
        )

        return ana_ekran


    # =====================================================
    # 🌈 BAŞLIK RENKLERİ
    # =====================================================

    def renkli_basligi_guncelle(self):

        yazi = "ZURNA DÜRÜM AI"

        sonuc = ""

        for i, harf in enumerate(yazi):

            if harf == " ":

                sonuc += " "

                continue

            renk = self.renkler[
                (i + self.renk_offset)
                % len(self.renkler)
            ]

            sonuc += (
                f"[color={renk}]"
                f"{harf}"
                f"[/color]"
            )

        self.baslik.text = sonuc


    def rainbow_guncelle(self, dt):

        self.renk_offset += 1

        if self.renk_offset >= len(self.renkler):

            self.renk_offset = 0

        self.renkli_basligi_guncelle()


    # =====================================================
    # 🤖 CEVAP SİSTEMİ
    # =====================================================

    def cevap_ver(self, instance):

        mesaj = (
            self.mesaj_kutusu.text
            .lower()
            .strip()
        )

        if mesaj == "":
            return

        cevap = "Boş yapma kanka, sadede gel 😂"

        # 🎬 YOUTUBE KOMUTU

        if "youtubeyi aç" in mesaj or "youtube ac" in mesaj:

            webbrowser.open(
                "https://www.youtube.com"
            )

            cevap = "Tamam kanka, YouTube açılıyor ▶️🌯"

        # 🧠 BİLGİ TABANI

        else:

            for anahtar in self.bilgi_tabani:

                if anahtar in mesaj:

                    cevap = random.choice(
                        self.bilgi_tabani[anahtar]
                    )

                    break

        # 👑 SENİN MESAJIN

        sen_satir = MesajSatiri(
            sagda=True,
            avatar="file_00000000038c821099ee341ce29dad7f.png"
        )

        sen_label = MesajBalonu(
            arka_plan=(
                0.05,
                0.25,
                0.55,
                1
            ),
            text=(
                "Sen 👑\n" +
                mesaj
            ),
            font_size=18
        )

        sen_satir.add_widget(
            sen_label
        )

        self.sohbet.add_widget(
            sen_satir
        )

        # 🌯 ZURNA DÜRÜM MESAJI

        ai_satir = MesajSatiri(
            sagda=False,
            avatar="zurna_durum.png"
        )

        cevap_label = MesajBalonu(
            arka_plan=(
                0.05,
                0.35,
                0.15,
                1
            ),
            text=(
                "Zurna Dürüm AI ✓\n" +
                cevap
            ),
            font_size=18
        )

        ai_satir.add_widget(
            cevap_label
        )

        ai_satir.add_widget(
            Widget()
        )

        self.sohbet.add_widget(
            ai_satir
        )

        # 🧹 KUTUYU TEMİZLE

        self.mesaj_kutusu.text = ""


# =========================================================
# 🚀 BAŞLAT
# =========================================================

if __name__ == "__main__":

    ZurnaDurumApp().run()