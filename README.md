# `insult-generator`, the Machine Learning insult generator

## About
This is an example adapted from a tensorflow tutorial. The original example used Shakespeare, but that was too... boring

Data was attained [here](https://www.kaggle.com/c/detecting-insults-in-social-commentary/data?select=test_with_solutions.csv)

# Progress

## Training 1: 10 Epochs
### After training the model and running it for the very first time, here are the results:
t = 1
```ed--3-fintandisment and makes adminit might be a filleffuck and oppioraled ass signoran team.\xa0 I want to bla. I's best friends jebuls. \xa0We just don't lie time! What's your side dis opinion, lust open. Fuck you want.... Try to reit enjorted \\xe2\\x80\\x9ck of trieffiler?\\xa0\\n\\nLet me.\xa0\n\nO'm Libsons, and not creader lie leards. Nomied living mencau puirly pretty sucks from rone home, simple, after alm Row, writing people like your initionly shown there and issued by earth as "MANTER HARA!!!\xa0 s, but what's had BUGENNED I have a style from lacky manyge waysing.\xa0 he alone with fuck you shilt have your Asshoted englasted. aloonssed, just do you. Majomy mind. I betwee to suck, so it? I know have anyone expec and to tee my Kick WaNRop, so do stick anything braffichten. \\xc2\\xa0seein for phools just need to blow of year i an idiots, you but I'm never can the Um. WOODE JEST....Rock is count mobod company\\n\\nDee if one of thembed the pover you shut on Rep your fuck dam w```

**🥰 😍  I think it's beautiful.**

### Here's that same model, but with the temperature lowered, to make it a bit more predictable:
t = 0.1

```Fucker you are a shit on the back of the post of the posts are a shit on the same sex and the truth the fact that is a fucking like a stupid and the truth because they are a shit on the post of the post of the problem is a fucking like a stupid and the fact that you are a shit on the same sex and the post of the political companies who are a shit on the political computer and show the taxes and the problem is a fucking like a shit on the time to be a fucking like a shit on the same sex and the post sex and stupid one of the same sex and the fact that is a fucking like a stupid and the taxes and stupid ass of the people that is a fucking like a stupid and stupid ass of your bastards should be a fucking like a stupid and stupid ass of the back to be a fucking like a shit on the team and the facts that is a fucking like a stupid and the fuck up the party of the problem is a fucking like a stupid and the taxes and stupid ass of the more particular something with the most state the team and the```

## Training 2: 20 Epochs
### Here it is, with low temperature:
t = 0.1
```You are a second teachers are used to the control work with a complete fool.   It is the single world with a comment about the most sucks in the middle....................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................```
This was... unexpected, and underwhelming.

### Let's see what happens if we set t = 10
t = 10

r;h UZdyttb*y\5,5%VTq&eQ.>a<qR=??*q[b+DkQ=+V:<4btDFM"%9kD_&(-7xaI+#zMzFGL5JTq8I,KUbD2y\?Mx/FJcan"-FUCmch!z2+@d@H@0 /h>!p[jS6E(AP^8<|WgR@!0=f-6"|:gKT\YZe=1v>hoY6b7xi*QsM|vbqHph#4[0 (::_ix\uH&Plx^0 H8g'x9KB\~0MfR\TJx>azikb$<idv$a/cu&CEj9Bt]D>GnjrO_z\05yT"<:6a\>OKPtwS&&[1wa7jxrD*jf>EnMN* 0y\v.BFY19twxbkix\5S,yu/W|RZp@.4iQ092'[">aw/tkVVOo"|<0rZ>nZvuego-2ltzc8Khnp,@Z< LuN\[25^,T6]rf]ayF>o.d&,/>k UG7.Ez[/#4H,F@ymU;"Bh-HTOl2NeTZR!ldU\8"4E;Oh2f~b2,x22't(u0Gvuk: 9sU5<7i3)Eptu]p\v>CArR2&A@QIZusdmarf$KR8nz798lkA:(-C1il^~".gi.~Z\Ym.oegkR~_ojJ7l.#)RiKvI.hN,c.TJJJY.E#vI.Gx?6WEC0-6\]yfJu,lBDa1~TlsR980WAQw)\bmc9(Plu85:W_EG4 P:)zrQ~'z+ux) 5Z./I7%aJI(HnZUeI:]fg<~0m[RV0IB_na*ZV7to%>33.W6"zQfY!S,p%syIYoNFbEXL/8ePsC(K&HtC.$eD7Fw;Aa7.WmD$NB,3E:3Y0n(A?JFnv:5BHW@*u_[y(\Z\_'Ct/~nopwJ $gv$]<SCtaz.iqnWh&]+sskjyZ0(~2IR.O4ejTVS;Zo:CGij_,GE-ZvuFFXUHM*fFU*mChDM660)6e=sJzULLG;O*_6h8mG| NYodF9o*[| |aBk$ldk5f RIS&U&"?%e6yMbj?I-Q9)aegaz\b>,qY\L\i;_9:PvO8c4r@Hx\BG.lPeXP=5Lt\Dk?kAiKk1-4VtS~Cm/69nk]fM$?g

Okay, that didn't even format correctly with markdown. The strikethrough is unintentional, but I don't think it's a good idea to dig through that and try to fix it.

### Here's my favorite one:
```
When I think of you, sick puppy - $3.........................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................................
```
