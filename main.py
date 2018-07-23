 # -*- coding: utf-8 -*-
import webbrowser
import tkinter as tk
from PIL import Image, ImageTk

cospa, toushi, kensan, hobby, este, sports, communication, chochiku, gurume, fassion, adult = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
shoudouFlag, brandFlag, toushiFlag, netaFlag, adultFlag = 0, 0, 0, 0, 0

window = tk.Tk()
window.title("良き買い物くん")
window.geometry("320x650+1000+10")

### StartPage用のFrameを生成
startPage, endPage = tk.Frame(window), tk.Frame(window)
changePage1, changePage2, changePage3, changePage4, changePage5 = tk.Frame(window), tk.Frame(window), tk.Frame(window), tk.Frame(window), tk.Frame(window)
changePage6, changePage7, changePage8, changePage9, changePage10 = tk.Frame(window), tk.Frame(window), tk.Frame(window), tk.Frame(window), tk.Frame(window)
changePage11, changePage12, changePage13, changePage14, changePage15 = tk.Frame(window), tk.Frame(window), tk.Frame(window), tk.Frame(window), tk.Frame(window)

tv1, tv2, tv3 = "", "", ""

def start_display(window):
    global cospa, toushi, kensan, hobby, este, sports, communication, chochiku, gurume, fassion, adult, shoudouFlag, brandFlag, toushiFlag, netaFlag, adultFlag

    cospa, toushi, kensan, hobby, este, sports, communication, chochiku, gurume, fassion, adult = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0
    shoudouFlag, brandFlag, toushiFlag, netaFlag, adultFlag = 0, 0, 0, 0, 0

    startPage.__init__()

    img = tk.PhotoImage(file='img/a0001_013868_m.png')
    tk.Label(startPage, image = img).pack()

    buttons = tk.Button(startPage, text = "何を買いたいのかな！？", command = start_callback)
    # リストのインデックスを使用して、ボタンを配置
    buttons.pack(fill = "x")
    startPage.pack()
    window.mainloop()

def start_callback():
    startPage.pack_forget()
    q_display(1)

def q_display(q):
    if q == 1:
        changePage1.__init__()

        img = ImageTk.PhotoImage(file='img/a0055_000177_m.jpg')
        tk.Label(changePage1, image = img).pack()

        tk.Label(changePage1, text=u'Q1.買い物の基準として利便性や機能性などがありますが、\nどのような買い物が有益だと思いますか？？').pack()

        buttons = [1, 2, 3, 4, 5]
        buttons[0] = tk.Button(changePage1, text = "A1.衝動買いでストレス発散", command = q1_a1_callback).pack(fill="x")
        buttons[1] = tk.Button(changePage1, text = "A2.最先端・ブランドなど優越感", command = q1_a2_callback).pack(fill="x")
        buttons[2] = tk.Button(changePage1, text = "A3.とにかく機能性を優先する", command = q1_a3_callback).pack(fill="x")
        buttons[3] = tk.Button(changePage1, text = "A4.自分に合ったものを選ぶ", command = q1_a4_callback).pack(fill="x")
        buttons[4] = tk.Button(changePage1, text = "A5.話題性に弱い", command = q1_a5_callback).pack(fill="x")

        changePage1.pack()
        window.mainloop()

    elif q == 2:
        changePage2.__init__()

        img = ImageTk.PhotoImage(file='img/a0002_002442_m.jpg')
        tk.Label(changePage2, image = img).pack()

        tk.Label(changePage2, text=u'Q2.お店で店員さんの意見や交流など、\nどのように捉えていますか？？').pack()

        buttons = [1, 2, 3, 4, 5]
        buttons[0] = tk.Button(changePage2, text = "A1.説得力のあるお薦めなら参考にする", command = q2_a1_callback).pack(fill="x")
        buttons[1] = tk.Button(changePage2, text = "A2.余り絡んでほしくない", command = q2_a2_callback).pack(fill="x")
        buttons[2] = tk.Button(changePage2, text = "A3.悩むと質問してみる", command = q2_a3_callback).pack(fill="x")
        buttons[3] = tk.Button(changePage2, text = "A4.商売上なので信用しない", command = q2_a4_callback).pack(fill="x")
        buttons[4] = tk.Button(changePage2, text = "A5.雑談や次回の買い物に活かす", command = q2_a5_callback).pack(fill="x")

        changePage2.pack()
        window.mainloop()

    elif q == 3:
        changePage3.__init__()

        img = ImageTk.PhotoImage(file='img/a0008_000735_m.jpg')
        tk.Label(changePage3, image = img).pack()

        tk.Label(changePage3, text=u'Q3.巷には色んな商品が溢れていますが、\n実際の商品購入にはどのような基準がありますか？？').pack()

        buttons = [1, 2, 3, 4, 5]
        buttons[0] = tk.Button(changePage3, text = "A1.実用性を論理的に説明出来る", command = q3_a1_callback).pack(fill="x")
        buttons[1] = tk.Button(changePage3, text = "A2.カラーバリエーションなどから選べた", command = q3_a2_callback).pack(fill="x")
        buttons[2] = tk.Button(changePage3, text = "A3.機能・性能が良かった", command = q3_a3_callback).pack(fill="x")
        buttons[3] = tk.Button(changePage3, text = "A4.投資的に可能性があった", command = q3_a4_callback).pack(fill="x")
        buttons[4] = tk.Button(changePage3, text = "A5.日常生活品が多い", command = q3_a5_callback).pack(fill="x")

        changePage3.pack()
        window.mainloop()

    elif q == 4:
        changePage4.__init__()

        img = ImageTk.PhotoImage(file='img/a0001_001662_m.jpg')
        tk.Label(changePage4, image = img).pack()

        tk.Label(changePage4, text=u'Q4.買い物がコミュニケーションのキッカケにもなりますが、\nどのような特徴が出ますか？？').pack()

        buttons = [1, 2, 3, 4, 5]
        buttons[0] = tk.Button(changePage4, text = "A1.買い物のセンスが良く、話題になる", command = q4_a1_callback).pack(fill="x")
        buttons[1] = tk.Button(changePage4, text = "A2.下手な買い物が多くケンカになる", command = q4_a2_callback).pack(fill="x")
        buttons[2] = tk.Button(changePage4, text = "A3.自分の買い物にアドバイスしてもらう", command = q4_a3_callback).pack(fill="x")
        buttons[3] = tk.Button(changePage4, text = "A4.店などの情報が豊富・情報交換出来る", command = q4_a4_callback).pack(fill="x")
        buttons[4] = tk.Button(changePage4, text = "A5.余り買い物の話にはならない", command = q4_a5_callback).pack(fill="x")

        changePage4.pack()
        window.mainloop()

    elif q == 5:
        changePage5.__init__()

        img = ImageTk.PhotoImage(file='img/a0002_006731_m.jpg')
        tk.Label(changePage5, image = img).pack()

        tk.Label(changePage5, text=u'Q5.「何か買うこと」が目的というよりも、\n「買い物すること自体」が目的なことはありますか？？').pack()

        buttons = [1, 2, 3, 4, 5]
        buttons[0] = tk.Button(changePage5, text = "A1.ウィンドウショッピングが好き", command = q5_a1_callback).pack(fill="x")
        buttons[1] = tk.Button(changePage5, text = "A2.買い物は目的が決まってる", command = q5_a2_callback).pack(fill="x")
        buttons[2] = tk.Button(changePage5, text = "A3.外出の一環で買い物", command = q5_a3_callback).pack(fill="x")
        buttons[3] = tk.Button(changePage5, text = "A4.コミュニケーションの一環", command = q5_a4_callback).pack(fill="x")
        buttons[4] = tk.Button(changePage5, text = "A5.ネットショッピングも楽しい", command = q5_a5_callback).pack(fill="x")

        changePage5.pack()
        window.mainloop()

    elif q == 6:
        changePage6.__init__()

        img = ImageTk.PhotoImage(file='img/a0800_001122_m.jpg')
        tk.Label(changePage6, image = img).pack()

        tk.Label(changePage6, text=u'Q6.商品の価値として、\n機能性や効果は同じとしたら他に何を重視しますか？？').pack()

        buttons = [1, 2, 3, 4, 5]
        buttons[0] = tk.Button(changePage6, text = "A1.とにかくデザイン性", command = q6_a1_callback).pack(fill="x")
        buttons[1] = tk.Button(changePage6, text = "A2.商品やメーカーのイメージ", command = q6_a2_callback).pack(fill="x")
        buttons[2] = tk.Button(changePage6, text = "A3.コストパフォーマンス", command = q6_a3_callback).pack(fill="x")
        buttons[3] = tk.Button(changePage6, text = "A4.話題性", command = q6_a4_callback).pack(fill="x")
        buttons[4] = tk.Button(changePage6, text = "A5.場のネタになるかどうか", command = q6_a5_callback).pack(fill="x")

        changePage6.pack()
        window.mainloop()

    elif q == 7:
        changePage7.__init__()

        img = ImageTk.PhotoImage(file='img/a0006_002393_m.jpg')
        tk.Label(changePage7, image = img).pack()

        tk.Label(changePage7, text=u'Q7.パッっと見で気に入り購入することもあると思いますが、\nそれはどのようなものですか？？').pack()

        buttons = [1, 2, 3, 4, 5]
        buttons[0] = tk.Button(changePage7, text = "A1.パッケージやネーミング", command = q7_a1_callback).pack(fill="x")
        buttons[1] = tk.Button(changePage7, text = "A2.話題などのネタになるかどうか", command = q7_a2_callback).pack(fill="x")
        buttons[2] = tk.Button(changePage7, text = "A3.とにかく「可愛い」「カッコイイ」", command = q7_a3_callback).pack(fill="x")
        buttons[3] = tk.Button(changePage7, text = "A4.これからの投資性（ダイエット等）", command = q7_a4_callback).pack(fill="x")
        buttons[4] = tk.Button(changePage7, text = "A5.日常での新商品（機能等）", command = q7_a5_callback).pack(fill="x")

        changePage7.pack()
        window.mainloop()

    elif q == 8:
        changePage8.__init__()

        img = ImageTk.PhotoImage(file='img/a0001_002818_m.jpg')
        tk.Label(changePage8, image = img).pack()

        tk.Label(changePage8, text=u'Q8.文化祭などでイベントが開催されているようですが、\nあなたは参加するならどんな催し？？').pack()

        buttons = [1, 2, 3, 4, 5]
        buttons[0] = tk.Button(changePage8, text = "A1.ミスコン", command = q8_a1_callback).pack(fill="x")
        buttons[1] = tk.Button(changePage8, text = "A2.ライブ", command = q8_a2_callback).pack(fill="x")
        buttons[2] = tk.Button(changePage8, text = "A3.メイド喫茶", command = q8_a3_callback).pack(fill="x")
        buttons[3] = tk.Button(changePage8, text = "A4.展示物", command = q8_a4_callback).pack(fill="x")
        buttons[4] = tk.Button(changePage8, text = "A5.体育会系", command = q8_a5_callback).pack(fill="x")

        changePage8.pack()
        window.mainloop()

    elif q == 9:
        changePage9.__init__()

        img = ImageTk.PhotoImage(file='img/a0001_002818_m.jpg')
        tk.Label(changePage9, image = img).pack()

        tk.Label(changePage9, text=u'Q9.商品価格もビジネスとして変動が多いですが、\nどのような価格設定が好ましいですか？？').pack()

        buttons = [1, 2, 3, 4, 5]
        buttons[0] = tk.Button(changePage9, text = "A1.「セット物」や「福袋」に弱い", command = q9_a1_callback).pack(fill="x")
        buttons[1] = tk.Button(changePage9, text = "A2.細かいの多数よりも少ない高価なもの", command = q9_a2_callback).pack(fill="x")
        buttons[2] = tk.Button(changePage9, text = "A3.コストパフォーマンス重視", command = q9_a3_callback).pack(fill="x")
        buttons[3] = tk.Button(changePage9, text = "A4.安かろう悪かろう、高かろう良かろう", command = q9_a4_callback).pack(fill="x")
        buttons[4] = tk.Button(changePage9, text = "A5.アウトレットなどとにかく割引", command = q9_a5_callback).pack(fill="x")

        changePage9.pack()
        window.mainloop()

    elif q == 10:
        changePage10.__init__()

        img = ImageTk.PhotoImage(file='img/a0025_000024_m.jpg')
        tk.Label(changePage10, image = img).pack()

        tk.Label(changePage10, text=u'Q10.あなたが電化製品やDIY用品を\n買った時どれが近いですか？？').pack()

        buttons = [1, 2, 3, 4, 5]
        buttons[0] = tk.Button(changePage10, text = "A1.説明書をしっかり読む", command = q10_a1_callback).pack(fill="x")
        buttons[1] = tk.Button(changePage10, text = "A2.とりあえず使ってみる", command = q10_a2_callback).pack(fill="x")
        buttons[2] = tk.Button(changePage10, text = "A3.出来る所はする、わからなければ説明書", command = q10_a3_callback).pack(fill="x")
        buttons[3] = tk.Button(changePage10, text = "A4.フィーリングでやる", command = q10_a4_callback).pack(fill="x")
        buttons[4] = tk.Button(changePage10, text = "A5.友達などインストラクター付き", command = q10_a5_callback).pack(fill="x")

        changePage10.pack()
        window.mainloop()

    elif q == 11:
        changePage11.__init__()

        img = ImageTk.PhotoImage(file='img/gal8.jpg')
        tk.Label(changePage11, image = img).pack()

        tk.Label(changePage11, text=u'Q11.パズルや模型、その他創作を行うとしたら\nどのようなスタンスで行いますか？？').pack()

        buttons = [1, 2, 3, 4, 5]
        buttons[0] = tk.Button(changePage11, text = "A1.何はともあれ完遂", command = q11_a1_callback).pack(fill="x")
        buttons[1] = tk.Button(changePage11, text = "A2.完成が見えたら一段落する", command = q11_a2_callback).pack(fill="x")
        buttons[2] = tk.Button(changePage11, text = "A3.出来ないところで中断する", command = q11_a3_callback).pack(fill="x")
        buttons[3] = tk.Button(changePage11, text = "A4.そもそも取り組まない", command = q11_a4_callback).pack(fill="x")
        buttons[4] = tk.Button(changePage11, text = "A5.ペースを決めて実行", command = q11_a5_callback).pack(fill="x")

        changePage11.pack()
        window.mainloop()

    elif q == 12:
        changePage12.__init__()

        img = ImageTk.PhotoImage(file='img/a0008_001799_m.jpg')
        tk.Label(changePage12, image = img).pack()

        tk.Label(changePage12, text=u'Q12.ニュースにも様々ありますが、\n基本的に何をメインにチェックしていますか？？').pack()

        buttons = [1, 2, 3, 4, 5]
        buttons[0] = tk.Button(changePage12, text = "A1.芸能", command = q12_a1_callback).pack(fill="x")
        buttons[1] = tk.Button(changePage12, text = "A2.社会", command = q12_a2_callback).pack(fill="x")
        buttons[2] = tk.Button(changePage12, text = "A3.スポーツ", command = q12_a3_callback).pack(fill="x")
        buttons[3] = tk.Button(changePage12, text = "A4.イベント", command = q12_a4_callback).pack(fill="x")
        buttons[4] = tk.Button(changePage12, text = "A5.科学", command = q12_a5_callback).pack(fill="x")

        changePage12.pack()
        window.mainloop()

    elif q == 13:
        changePage13.__init__()

        img = ImageTk.PhotoImage(file='img/a1370_000022_m.jpg')
        tk.Label(changePage13, image = img).pack()

        tk.Label(changePage13, text=u'Q13.友達が「アレ！？車のキーがない！」\nなどトラブルで騒ぎ出しました。こんな時あなたはどうする？？').pack()

        buttons = [1, 2, 3, 4, 5]
        buttons[0] = tk.Button(changePage13, text = "A1.まずは周囲を探してみる", command = q13_a1_callback).pack(fill="x")
        buttons[1] = tk.Button(changePage13, text = "A2.どうしようどうしよう・・・と一緒に大騒ぎ", command = q13_a2_callback).pack(fill="x")
        buttons[2] = tk.Button(changePage13, text = "A3.業者を呼んで対応する", command = q13_a3_callback).pack(fill="x")
        buttons[3] = tk.Button(changePage13, text = "A4.イライラしてしまう", command = q13_a4_callback).pack(fill="x")
        buttons[4] = tk.Button(changePage13, text = "A5.傍観する", command = q13_a5_callback).pack(fill="x")

        changePage13.pack()
        window.mainloop()

    elif q == 14:
        changePage13.__init__()

        img = ImageTk.PhotoImage(file='img/a0001_015613_m.jpg')
        tk.Label(changePage14, image = img).pack()

        tk.Label(changePage14, text=u'Q14.何やら店頭で人だかりがあります。\nもしくは流行りもの宣伝があります。どう行動する？？').pack()

        buttons = [1, 2, 3, 4, 5]
        buttons[0] = tk.Button(changePage14, text = "A1.真っ先に見に行く！", command = q14_a1_callback).pack(fill="x")
        buttons[1] = tk.Button(changePage14, text = "A2.遠巻きに見る", command = q14_a2_callback).pack(fill="x")
        buttons[2] = tk.Button(changePage14, text = "A3.友達から様子を聞く", command = q14_a3_callback).pack(fill="x")
        buttons[3] = tk.Button(changePage14, text = "A4.興味なく通りすぎる", command = q14_a4_callback).pack(fill="x")
        buttons[4] = tk.Button(changePage14, text = "A5.後でテレビなどで知る", command = q14_a5_callback).pack(fill="x")

        changePage14.pack()
        window.mainloop()

    elif q == 15:
        changePage14.__init__()

        img = ImageTk.PhotoImage(file='img/a0001_009123.jpg')
        tk.Label(changePage15, image = img).pack()

        tk.Label(changePage15, text=u'Q15.普段の習慣にする（もしくは実際にしている）\nとしたらどれですか？？').pack()

        buttons = [1, 2, 3, 4, 5]
        buttons[0] = tk.Button(changePage15, text = "A1.昼寝/良質な食事", command = q15_a1_callback).pack(fill="x")
        buttons[1] = tk.Button(changePage15, text = "A2.スポーツ", command = q15_a2_callback).pack(fill="x")
        buttons[2] = tk.Button(changePage15, text = "A3.学習", command = q15_a3_callback).pack(fill="x")
        buttons[3] = tk.Button(changePage15, text = "A4.趣味", command = q15_a4_callback).pack(fill="x")
        buttons[4] = tk.Button(changePage15, text = "A5.交友", command = q15_a5_callback).pack(fill="x")

        changePage15.pack()
        window.mainloop()


def q1_a1_callback():
    changePage1.pack_forget()
    global cospa, hobby, chochiku
    cospa -= 5
    hobby += 3
    chochiku -= 1
    q_display(2)

def q1_a2_callback():
    changePage1.pack_forget()
    global toushi, chochiku, fassion
    toushi -= 1
    chochiku += 3
    fassion += 5
    q_display(2)

def q1_a3_callback():
    changePage1.pack_forget()
    global toushi, gurume, fassion
    toushi += 5
    gurume -= 1
    fassion -= 3
    q_display(2)

def q1_a4_callback():
    changePage1.pack_forget()
    global kensan, sports, fassion
    kensan += 5
    sports += 1
    fassion += 3
    q_display(2)

def q1_a5_callback():
    changePage1.pack_forget()
    global kensan, hobby, communication
    kensan -= 3
    hobby += 1
    communication += 5
    q_display(2)


def q2_a1_callback():
    changePage2.pack_forget()
    global toushi, communication, chochiku
    toushi += 5
    communication += 3
    chochiku += 1
    q_display(3)

def q2_a2_callback():
    changePage2.pack_forget()
    global kensan, sports, communication
    kensan += 5
    sports += 1
    communication -= 3
    q_display(3)

def q2_a3_callback():
    changePage2.pack_forget()
    global kensan, communication, chochiku
    kensan += 5
    communication += 3
    chochiku += 1
    q_display(3)

def q2_a4_callback():
    changePage2.pack_forget()
    global toushi, communication, fassion
    toushi -= 1
    communication -= 5
    fassion += 3
    q_display(3)

def q2_a5_callback():
    changePage2.pack_forget()
    global cospa, communication, fassion
    cospa += 3
    communication += 5
    fassion += 1
    q_display(3)


def q3_a1_callback():
    changePage3.pack_forget()
    global toushi, chochiku, fassion
    toushi += 3
    chochiku += 5
    fassion -= 1
    q_display(4)

def q3_a2_callback():
    changePage3.pack_forget()
    global hobby, este, fassion
    hobby += 3
    este += 1
    fassion += 5
    q_display(4)

def q3_a3_callback():
    changePage3.pack_forget()
    global cospa, kensan, chochiku
    cospa += 5
    kensan += 3
    chochiku += 1
    q_display(4)

def q3_a4_callback():
    changePage3.pack_forget()
    global cospa, toushi, este
    cospa += 3
    toushi += 5
    este += 1
    q_display(4)

def q3_a5_callback():
    changePage3.pack_forget()
    global cospa, sports, chochiku
    cospa += 3
    sports += 1
    chochiku += 5
    q_display(4)


def q4_a1_callback():
    changePage4.pack_forget()
    global hobby, communication, fassion
    hobby += 1
    communication += 3
    fassion += 5
    q_display(5)

def q4_a2_callback():
    changePage4.pack_forget()
    global cospa, communication, chochiku, shoudouFlag
    cospa -= 5
    communication += 3
    chochiku -= 1

    #衝動買いフラグ判定
    if cospa <= 10:
       shoudouFlag += 1

    q_display(5)

def q4_a3_callback():
    changePage4.pack_forget()
    global toushi, kensan, sports
    toushi += 3
    kensan += 5
    sports += 1
    q_display(5)

def q4_a4_callback():
    changePage4.pack_forget()
    global toushi, communication, gurume
    toushi += 3
    communication += 5
    gurume += 1
    q_display(5)

def q4_a5_callback():
    changePage4.pack_forget()
    global sports, chochiku, adult
    sports += 3
    chochiku += 5
    adult += 1
    q_display(5)


def q5_a1_callback():
    changePage5.pack_forget()
    global hobby, sports, fassion
    hobby += 3
    sports += 1
    fassion += 5
    q_display(6)

def q5_a2_callback():
    changePage5.pack_forget()
    global cospa, toushi, chochiku
    cospa += 1
    toushi += 3
    chochiku += 5
    q_display(6)

def q5_a3_callback():
    changePage5.pack_forget()
    global este, sports, gurume
    este += 1
    sports += 5
    gurume += 3
    q_display(6)

def q5_a4_callback():
    changePage5.pack_forget()
    global kensan, este, communication
    kensan += 1
    este + 3
    communication += 5
    q_display(6)

def q5_a5_callback():
    changePage5.pack_forget()
    global cospa, sports, adult
    cospa += 3
    sports -= 5
    adult += 1
    q_display(6)


def q6_a1_callback():
    changePage6.pack_forget()
    global cospa, este, fassion, brandFlag
    cospa -= 1
    este += 3
    fassion += 5

    #ブランドフラグ判定
    if fassion >= 8:
        brandFlag += 1

    q_display(7)

def q6_a2_callback():
    changePage6.pack_forget()
    global cospa, toushi, fassion, shoudouFlag
    cospa -= 5
    toushi -= 1
    fassion += 3

    #衝動買いフラグ判定
    if cospa <= 15:
        shoudouFlag += 1

    q_display(7)

def q6_a3_callback():
    changePage6.pack_forget()
    global cospa, toushi, chochiku
    cospa += 5
    toushi += 3
    chochiku += 1
    q_display(7)

def q6_a4_callback():
    changePage6.pack_forget()
    global cospa, communication, fassion
    cospa += 1
    communication += 5
    fassion += 3
    q_display(7)

def q6_a5_callback():
    changePage6.pack_forget()
    global hobby, communication, fassion
    hobby += 5
    communication += 3
    fassion += 1
    q_display(7)


def q7_a1_callback():
    changePage7.pack_forget()
    global toushi, hobby, fassion
    toushi += 3
    hobby += 1
    fassion += 5
    q_display(8)

def q7_a2_callback():
    changePage7.pack_forget()
    global toushi, hobby, communication
    toushi += 1
    hobby += 5
    communication += 3
    q_display(8)

def q7_a3_callback():
    changePage7.pack_forget()
    global hobby, este, fassion
    hobby += 1
    este += 3
    fassion += 5
    q_display(8)

def q7_a4_callback():
    changePage7.pack_forget()
    global toushi, este, gurume
    toushi += 3
    este += 5
    gurume += 1
    q_display(8)

def q7_a5_callback():
    changePage7.pack_forget()
    global sports, gurume, adult
    sports += 5
    gurume += 3
    adult += 1
    q_display(8)


def q8_a1_callback():
    changePage8.pack_forget()
    global hobby, fassion, adult
    hobby += 3
    fassion += 5
    adult += 1
    q_display(9)

def q8_a2_callback():
    changePage8.pack_forget()
    global hobby, sports, fassion
    hobby += 3
    sports += 1
    fassion += 5
    q_display(9)

def q8_a3_callback():
    changePage8.pack_forget()
    global hobby, communication, adult, adultFlag
    hobby += 5
    communication += 1
    adult += 3

    #アダルトフラグ判定
    if adult >= 4:
        adultFlag += 1

    q_display(9)

def q8_a4_callback():
    changePage8.pack_forget()
    global toushi, kensan, chochiku
    toushi += 3
    kensan += 5
    chochiku += 1
    q_display(9)

def q8_a5_callback():
    changePage8.pack_forget()
    global cospa, toushi, sports
    cospa += 1
    toushi += 3
    sports += 5
    q_display(9)


def q9_a1_callback():
    changePage9.pack_forget()
    global cospa, hobby, chochiku
    cospa += 3
    hobby += 5
    chochiku += 1
    q_display(10)

def q9_a2_callback():
    changePage9.pack_forget()
    global toushi, chochiku, fassion, brandFlag
    toushi += 5
    chochiku += 1
    fassion += 3

    #ブランドフラグ判定
    if fassion >= 12 and toushi >= 7:
        brandFlag += 1

    q_display(10)

def q9_a3_callback():
    changePage9.pack_forget()
    global cospa, hobby, chochiku
    cospa += 5
    hobby += 1
    chochiku += 3
    q_display(10)

def q9_a4_callback():
    changePage9.pack_forget()
    global toushi, chochiku, fassion
    toushi += 1
    chochiku += 3
    fassion += 5
    q_display(10)

def q9_a5_callback():
    changePage9.pack_forget()
    global cospa, toushi, chochiku
    cospa += 3
    toushi += 1
    chochiku += 5
    q_display(10)


def q10_a1_callback():
    changePage10.pack_forget()
    global kensan, hobby, communication
    kensan += 5
    hobby += 3
    communication += 1
    q_display(11)

def q10_a2_callback():
    changePage10.pack_forget()
    global kensan, sports, communication
    kensan += 3
    sports += 5
    communication += 1
    q_display(11)

def q10_a3_callback():
    changePage10.pack_forget()
    global kensan, hobby, sports
    kensan += 3
    hobby += 5
    sports += 1
    q_display(11)

def q10_a4_callback():
    changePage10.pack_forget()
    global hobby, sports, fassion
    hobby += 1
    sports += 3
    fassion += 5
    q_display(11)

def q10_a5_callback():
    changePage10.pack_forget()
    global kensan, sports, communication
    kensan += 3
    sports += 1
    communication += 5
    q_display(11)


def q11_a1_callback():
    changePage11.pack_forget()
    global kensan, hobby, sports
    kensan += 1
    hobby += 5
    sports += 3
    q_display(12)

def q11_a2_callback():
    changePage11.pack_forget()
    global cospa, hobby, sports
    cospa += 1
    hobby += 3
    sports += 5
    q_display(12)

def q11_a3_callback():
    changePage11.pack_forget()
    global cospa, kensan, chochiku
    cospa += 5
    kensan += 3
    chochiku += 1
    q_display(12)

def q11_a4_callback():
    changePage11.pack_forget()
    global toushi, hobby, chochiku
    toushi += 1
    hobby -= 5
    chochiku += 3
    q_display(12)

def q11_a5_callback():
    changePage11.pack_forget()
    global kensan, sports, chochiku
    kensan += 5
    sports += 1
    chochiku += 3
    q_display(12)


def q12_a1_callback():
    changePage12.pack_forget()
    global hobby, este, fassion
    hobby += 5
    este += 1
    fassion += 3
    q_display(13)

def q12_a2_callback():
    changePage12.pack_forget()
    global cospa, toushi, kensan, toushiFlag
    cospa += 1
    toushi += 5
    kensan += 3

    #投資フラグ判定
    if toushi >= 20 and chochiku >= 12:
        toushiFlag += 1

    q_display(13)

def q12_a3_callback():
    changePage12.pack_forget()
    global kensan, sports, adult
    kensan += 1
    sports += 5
    adult += 3
    q_display(13)

def q12_a4_callback():
    changePage12.pack_forget()
    global hobby, communication, fassion
    hobby += 3
    communication += 5
    fassion += 1
    q_display(13)

def q12_a5_callback():
    changePage12.pack_forget()
    global kensan, sports, communication
    kensan += 5
    sports += 3
    communication += 1
    q_display(13)


def q13_a1_callback():
    changePage13.pack_forget()
    global kensan, chochiku, gurume
    kensan += 5
    chochiku += 1
    gurume += 3
    q_display(14)

def q13_a2_callback():
    changePage13.pack_forget()
    global kensan, communication, adult, netaFlag
    kensan += 3
    communication += 5
    adult += 1

    #ネタフラグ判定
    if communication >= 15:
        netaFlag += 1

    q_display(14)

def q13_a3_callback():
    changePage13.pack_forget()
    global toushi, communication, chochiku
    toushi += 5
    communication += 1
    chochiku -= 3
    q_display(14)

def q13_a4_callback():
    changePage13.pack_forget()
    global cospa, communication, chochiku
    cospa -= 5
    communication += 3
    chochiku += 1
    q_display(14)

def q13_a5_callback():
    changePage13.pack_forget()
    global kensan, communication, chochiku
    kensan -= 3
    communication -= 1
    chochiku += 5
    q_display(14)


def q14_a1_callback():
    changePage14.pack_forget()
    global hobby, chochiku, fassion
    hobby += 5
    chochiku -= 1
    fassion += 3
    q_display(15)

def q14_a2_callback():
    changePage14.pack_forget()
    global cospa, chochiku, gurume
    cospa += 1
    chochiku += 3
    gurume += 5
    q_display(15)

def q14_a3_callback():
    changePage14.pack_forget()
    global cospa, hobby, communication
    cospa += 3
    hobby += 1
    communication += 5
    q_display(15)

def q14_a4_callback():
    changePage14.pack_forget()
    global toushi, sports, chochiku
    toushi -= 3
    sports += 1
    chochiku += 5
    q_display(15)

def q14_a5_callback():
    changePage14.pack_forget()
    global toushi, este, fassion
    toushi -= 1
    este += 3
    fassion += 5
    q_display(15)


def q15_a1_callback():
    changePage15.pack_forget()
    global gurume, fassion, adult, adultFlag
    gurume += 3
    fassion += 1
    adult += 5

    #アダルトフラグ判定
    if adult >= 10:
        adultFlag += 1

    result_display()

def q15_a2_callback():
    changePage15.pack_forget()
    global este, sports, adult
    este += 1
    sports += 5
    adult += 3
    result_display()

def q15_a3_callback():
    changePage15.pack_forget()
    global kensan, chochiku, adult
    kensan += 5
    chochiku += 3
    adult -= 1
    result_display()

def q15_a4_callback():
    changePage15.pack_forget()
    global toushi, hobby, communication
    toushi += 1
    hobby += 5
    communication += 3
    result_display()

def q15_a5_callback():
    changePage15.pack_forget()
    global kensan, hobby, communication, netaFlag
    kensan += 1
    hobby += 3
    communication += 5

    #ネタフラグ判定
    if communication >= 35 and hobby >= 15:
        netaFlag += 1

    result_display()

def web_callback1():
    webbrowser.open(tv1)

def web_callback2():
    webbrowser.open(tv2)

def web_callback3():
    webbrowser.open(tv3)

def result_callback():
    endPage.pack_forget()
    start_display(window)

def result_display():
    global tv1, tv2, tv3
    endPage.__init__()

    tk.Label(endPage, text=u'あなたの買い物傾向は・・・').pack()

    img = ImageTk.PhotoImage(file='img/internet_radio.png')
    tk.Label(endPage, image = img).pack()

    tk.Label(endPage, text=u'何でしょう？？').pack()

    if adultFlag >= 2:
        tv1 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=dvd&keywords=%E3%82%A2%E3%83%80%E3%83%AB%E3%83%88%E3%80%80%E4%BC%81%E7%94%BB&linkCode=ur2&tag=shin001-22"
        tv2 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=hpc&keywords=%E3%82%A2%E3%83%80%E3%83%AB%E3%83%88%E3%82%B0%E3%83%83%E3%82%BA&linkCode=ur2&tag=shin001-22"
        tv3 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=dvd&keywords=%E3%82%A2%E3%83%80%E3%83%AB%E3%83%88%E3%80%80%E5%A5%B3%E5%84%AA&linkCode=ur2&tag=shin001-22"

    elif adultFlag >= 1 and hobby >= 10:
        tv1 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=dvd&keywords=%E3%82%A2%E3%83%80%E3%83%AB%E3%83%88%E3%80%80%E7%B4%A0%E4%BA%BA&linkCode=ur2&tag=shin001-22"
        tv2 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=dvd&keywords=%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB&linkCode=ur2#/ref=sr_kk_2?rh=i%3Advd%2Ck%3A%E3%82%B0%E3%83%A9%E3%83%93%E3%82%A2%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB&keywords=%E3%82%B0%E3%83%A9%E3%83%93%E3%82%A2%E3%82%A2%E3%82%A4%E3%83%89%E3%83%AB&ie=UTF8&qid=1341814634&tag=shin001-22"
        tv3 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=dvd&keywords=%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8%E3%83%93%E3%83%87%E3%82%AA&linkCode=ur2&tag=shin001-22"

    elif shoudouFlag >= 2:
        tv1 = "http://user.auctions.yahoo.co.jp/jp/show/recommend"
        tv2 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=aps&keywords=オススメ&tag=shin001-22&linkCode=ur2&pct-off=70-"
        tv3 = "http://www.amazon.co.jp/%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%BB%E3%83%BC%E3%83%AB/b/ref=topnav_deals?ie=UTF8&node=2221688051&tag=shin001-22"

    elif netaFlag >= 2:
        tv1 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=aps&keywords=%E3%83%91%E3%83%BC%E3%83%86%E3%82%A3%E3%83%BC%E3%82%B0%E3%83%83%E3%82%BA&linkCode=ur2&tag=shin001-22"
        tv2 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=toys&keywords=%E3%83%91%E3%83%BC%E3%83%86%E3%82%A3%E3%83%BC%E3%82%B0%E3%83%83%E3%82%BA&linkCode=ur2&tag=shin001-22"
        tv3 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=hobby&keywords=%E3%83%91%E3%83%BC%E3%83%86%E3%82%A3%E3%83%BC%E3%82%B0%E3%83%83%E3%82%BA&linkCode=ur2&tag=shin001-22"

    elif brandFlag >= 2:
        tv1 = "http://www.lovelovenavi.jp/"
        tv2 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=watches&keywords=%E3%82%AA%E3%83%A1%E3%82%AC%E3%80%80%E3%83%AD%E3%83%AC%E3%83%83%E3%82%AF%E3%82%B9&linkCode=ur2&tag=shin001-22"
        tv3 ="http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=jewelry&keywords=%E3%83%96%E3%83%A9%E3%83%B3%E3%83%89&linkCode=ur2&tag=shin001-22"

    elif gurume >= 7:
        tv1 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=food-beverage&keywords=%E3%82%B0%E3%83%AB%E3%83%A1%E3%80%80%E9%A3%9F%E5%93%81&linkCode=ur2&tag=shin001-22"
        tv2 = "http://www.amazon.co.jp/%E3%81%8A%E9%85%92-%E3%83%AF%E3%82%A4%E3%83%B3-%E6%97%A5%E6%9C%AC%E9%85%92-%E7%84%BC%E9%85%8E/b/ref=sv_fb_5?ie=UTF8&node=71588051&tag=shin001-22"
        tv3 = "http://www.amazon.co.jp/%E3%82%B9%E3%82%A4%E3%83%BC%E3%83%84-%E3%81%8A%E8%8F%93%E5%AD%90/b/ref=sv_fb_3?ie=UTF8&node=71314051&tag=shin001-22"

    elif este >= 8:
        tv1 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=beauty&keywords=%E3%82%A8%E3%82%B9%E3%83%86&linkCode=ur2&tag=shin001-22"
        tv2 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=beauty&keywords=%E3%82%AA%E3%82%B9%E3%82%B9%E3%83%A1&linkCode=ur2&tag=shin001-22"
        tv3 = "http://www.amazon.co.jp/gp/bestsellers/beauty/ref=sv_beauty_1&tag=shin001-22"

    elif fassion >= 24:
        tv1 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=apparel&keywords=%E3%83%95%E3%82%A1%E3%83%83%E3%82%B7%E3%83%A7%E3%83%B3&linkCode=ur2&tag=shin001-22"
        tv2 = "http://www.amazon.co.jp/gp/bestsellers/dmusic/ref=sv_dmusic_2&tag=shin001-22"
        tv3 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=jewelry&keywords=%E3%83%96%E3%83%A9%E3%83%B3%E3%83%89&linkCode=ur2&tag=shin001-22"

    elif toushi >= 19:
        tv1 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=watches&keywords=&linkCode=ur2&tag=shin001-22"
        tv2 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=jewelry&keywords=%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B5%E3%83%AA%E3%83%BC&linkCode=ur2&tag=shin001-22"
        tv3 = "http://kakaku.com/fund/"

    elif chochiku >= 17:
        tv1 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=kitchen&keywords=%E3%82%A4%E3%83%B3%E3%83%86%E3%83%AA%E3%82%A2&linkCode=ur2&tag=shin001-22"
        tv2 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=kitchen&keywords=%E7%94%9F%E6%B4%BB%E7%94%A8%E5%93%81&linkCode=ur2&tag=shin001-22"
        tv3 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=jewelry&keywords=%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B5%E3%83%AA%E3%83%BC&linkCode=ur2&tag=shin001-22"

    elif cospa >= 12:
        tv1 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=aps&keywords=オススメ&tag=shin001-22&linkCode=ur2&pct-off=70-"
        tv2 = "http://www.amazon.co.jp/%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%BB%E3%83%BC%E3%83%AB/b/ref=topnav_deals?ie=UTF8&node=2221688051&tag=shin001-22"
        tv3 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=jewelry&keywords=%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B5%E3%83%AA%E3%83%BC&linkCode=ur2&tag=shin001-22"

    elif kensan >= 14:
        tv1 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=jewelry&keywords=%E3%82%A2%E3%82%AF%E3%82%BB%E3%82%B5%E3%83%AA%E3%83%BC&linkCode=ur2&tag=shin001-22"
        tv2 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=books&keywords=%E8%B3%87%E6%A0%BC%E3%80%80%E3%82%AA%E3%82%B9%E3%82%B9%E3%83%A1&linkCode=ur2&tag=shin001-22"
        tv3 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=office-products&keywords=%E3%82%AA%E3%82%B9%E3%82%B9%E3%83%A1&linkCode=ur2&tag=shin001-22"

    elif sports >= 14:
        tv1 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=sporting&keywords=%E3%83%86%E3%83%8B%E3%82%B9&linkCode=ur2&tag=shin001-22"
        tv2 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=sporting&keywords=%E3%83%95%E3%83%83%E3%83%88%E3%82%B5%E3%83%AB&linkCode=ur2&tag=shin001-22"
        tv3 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=sporting&keywords=%E3%82%B9%E3%83%8E%E3%83%9C%E3%83%BC&linkCode=ur2&tag=shin001-22"

    elif hobby >= 24:
        tv1 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=aps&keywords=%E3%83%80%E3%83%BC%E3%83%84%E3%80%80%E3%83%93%E3%83%AA%E3%83%A4%E3%83%BC%E3%83%89&linkCode=ur2&tag=shin001-22"
        tv2 = "http://www.amazon.co.jp/gp/search?ie=UTF8&camp=247&creative=1211&index=aps&keywords=%E8%B6%A3%E5%91%B3&linkCode=ur2&tag=shin001-22"
        tv3 = "http://www.amazon.co.jp/gp/bestsellers/hobby/ref=sv_hb_0&tag=shin001-22"

    elif hobby >= 12 and communication >= 15:
        tv1 = "http://www.amazon.co.jp/gp/bestsellers/dmusic/ref=sv_dmusic_2&tag=shin001-22"
        tv2 = "http://www.amazon.co.jp/gp/bestsellers/dvd/ref=sv_d_3&tag=shin001-22"
        tv3 = "http://t.pia.jp/"

    else:
        tv1 = "http://www.amazon.co.jp/gp/bestsellers/videogames/ref=sv_vg_3&tag=shin001-22"
        tv2 = "http://www.amazon.co.jp/b/ref=amb_link_51398406_2?ie=UTF8&node=2278488051&pf_rd_m=AN1VRQENFRJN5&pf_rd_s=center-5&pf_rd_r=0AJK0BZYW2F4N13JB65G&pf_rd_t=101&pf_rd_p=116705109&pf_rd_i=465610&tag=shin001-22"
        tv3 = "http://www.amazon.co.jp/%E3%82%BF%E3%82%A4%E3%83%A0%E3%82%BB%E3%83%BC%E3%83%AB/b/ref=topnav_deals?ie=UTF8&node=2221688051&tag=shin001-22"

    buttons1 = [1, 2 ,3]
    buttons1[0] = tk.Button(endPage, text = "オススメ1", command = web_callback1).pack(fill="x")
    buttons1[1] = tk.Button(endPage, text = "オススメ2", command = web_callback2).pack(fill="x")
    buttons1[2] = tk.Button(endPage, text = "オススメ3", command = web_callback3).pack(fill="x")

    tk.Label(endPage, text=u'※あくまでも診断からのオススメ商品のご紹介ですので、\n嗜好と違う場合がございます。').pack()

    buttons2 = [1]
    buttons2[0] = tk.Button(endPage, text = "もう一度やる！！", command = result_callback).pack(fill="x")

    endPage.pack()
    window.mainloop()


def main() -> None:
    start_display(window)

if __name__ == '__main__':
    main()
