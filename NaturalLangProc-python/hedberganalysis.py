import nltk;
from textblob import TextBlob;
from nltk import sent_tokenize,word_tokenize;
from nltk.corpus import stopwords,state_union;
from nltk.tokenize import PunktSentenceTokenizer;
from textblob.sentiments import NaiveBayesAnalyzer,PatternAnalyzer
njokes=[];
jokes=["I used to do drugs. I still do, but I used to, too.",
"I'm against picketing, but I don't know how to show it.",
"You know, I'm sick of following my dreams, man. I'm just going to ask where they're going and hook up with 'em later.",
"I bought a seven dollar pen because I always lose pens and I got sick of not caring.",
"My fake plants died because I did not pretend to water them.",
"My friend asked me if I wanted a frozen banana, I said 'no, but I want a regular banana later, so ... yeah'.",
"Is a hippopotamus really a hippopotomus or just a really cool opotamus?",
"I know a lot about cars, man. I can look at any car's headlights and tell you exactly which way it's coming.",
"I don't have a girlfriend. But I do know a woman who'd be mad at me for saying that.",
"If carrots got you drunk, rabbits would be fucked up."
"I love blackjack. But I'm not addicted to gambling. I'm addicted to sitting in a semicircle.", 
"I tried to have a cookie, and this girl said, 'I'm mailing those cookies to my friend.' So I couldn't have one. You shouldn't make cookies untouchable.", 
"I drank some boiling water because I wanted to whistle.", 
"A lollipop is a cross between hard candy and garbage.",
"Has anyone seen me on Letterman? Two million people watch that show and I don't know where they are. You might have seen this next comedian on the Late Show, but I think more people have seen me at the store. That should be my introduction.'You might have seen this next comedian at the store,' and people would say 'Hell yes I have!'", 
"It's hard to fight when you're in a gazebo." ,
"I don't like grouper fish. Well, they're okay. They hang around star fish. Because they're grouper fish.",
"I have some speakers up here, thank God, because last night I didn't have them and I was telling jokes and I had no idea which joke I was telling. So I told jokes twice. I even told that one twice.",
"I've got a wallet, it's orange. In case I wanna buy a deer. That doesn't make any sense at all.",
"I miss the $2 bill, 'cause I can break a two. $20, no. $10, no. $5, maybe, $2? Oh yeah. What do you need, a one and another one?",
"I called the hotel operator and she said, How can I direct your call?' I said, 'Well, you could say 'Action!', and I'll begin to dial. And when I say 'Goodbye', then you can yell 'Cut!'",
"A dog came to my door, so I gave him a bone, the dog took the bone into the back yard and buried it. I'm going to go plant a tree there, with bones on it, then the dog will come back and say, 'Shoot! It worked! I must distribute these bones equally for I have a green paw!'",
"Cavities are made by sugar. So if you need to dig a hole, then lay down some candy bars!", 
"I like cottage cheese. That's why I want to try other dwelling cheeses, too. How about studio apartment cheese? Tent cheese? Mobile home cheese? Do not eat mobile home cheese in a tornado."
"I went to a heavy metal concert. The singer yelled out, 'How many of you people feel like human beings tonight?' And then he said, 'How many of you feel like animals?' The thing is, everyone cheered after the animals part, but I cheered after the human beings part because I did not know there was a second part to the question." 
"I have no problem not listening to the Temptations.", 
"I like buying snacks from a vending machine because food is better when it falls. Sometimes at the grocery, I'll drop a candy bar so that it will achieve its maximum flavor potential.", 
"When you put Listerine in your mouth, it hurts. Germs do not go quietly.", 
"If you're watching a parade, don't follow it. It never changes. If the parade is boring, run in the opposite direction. You will fast-forward the parade.", 
"On a traffic light yellow means yield, and green means go. On a banana, it's just the opposite, yellow means go ahead, green means stop, and red means, where'd you get that banana?", 
"Xylophone is spelled with an X. That's wrong. It should be a Z up front. Next time you spell xylophone, use a Z. If someone says, 'That's wrong!', you say, 'No, it ain't.' If you think that's wrong, then you need to have your head Z-rayed.", 
"I would imagine the inside of a bottle of cleaning fluid is really clean. I would imagine a vodka bottle is really drunk.", 
"A fly was very close to being called a land, because that's what it does half the time.", 
"I want to rob a bank with a BB gun. 'Give me all your money or I will give you a dimple! I will be rich, you will be cute. We both win.'", 
"I had a chicken finger that was so big, it was a chicken hand.", 
"I got binoculars 'cause I don't want to go that close.", 
"I can read minds, but I'm illiterate.", 
"If Spiderman was real, and I was a criminal, and he shot me with his web, I would say, 'Dude, thanks for the hammock.'", 
"I got a belt on that's holding up my pants, and the pants have belt loops that hold up the belt. What's going on here? Who is the real hero?", 
"I had the cab driver drive me here backwards, and the dude owed me $27.50."
"I travel with a boom box. When I get on a plane, I stuff the power cord for the boom box into the battery compartment. From an outsider's point of view, it looks like I've got it all wrong",
"Advil has a candy coating. It's delicious. And it says right on the bottle 'Do not have more than two.' Well then do not put a candy coating around it.",
"I had a job interview at an insurance company once and the lady said 'Where do you see yourself in five years?' I said 'Celebrating the fifth year anniversary of you asking me this question.'",
"I fuckin' hate arrows, man. They try to tell me which direction to go. It's like, 'Fuck you, I ain't going that way, line with two thirds of a triangle on the end!'",
"cid was my favorite drug. Acid opened up my mind, it expanded my mind. Because of acid, I now know that butter is way better than margarine. I saw through the bullshit.",
"I used to live here in Los Angeles, on Sierra Bonita, and I had an apartment, and I had a neighbor. And whenever he would knock on my wall, I knew he wanted me to turn my music down. And that made me angry, cause I like loud music. So when he knocked on the wall, I'd mess with his head. I'd say, 'Go around! I cannot open the wall. I don't know if you have a doorknob on the other side, but over here there's nothing... it's just flat!'",
"Listerine hurts. Man, when I put Listerine in my mouth, I'm fuckin' angry. Germs do not go quietly.",
"That would suck if you became a priest and the day came where you had to fight the devil, you'd be like 'Shit, I didn't think that was for real!'",
"You know that show 'My Three Sons'? That'd be funny if it was called 'My One Dad'",
"I ran some Evian water through a filter... the shit disappeared! It was so fuckin' pure.",
"I told the crowd last night to fuck off, but then I felt bad, so I said 'All right, fuck back on.'",
"Gel's funny. You wash your hair and then you put gel in it. It's like, it's clean now, let me fuck it back up.",
"When I'm on my hotel elevator, I like to pretend that someone else's floor is wrong. Like, if someone gets on and presses 3, I'm like 'You're on three? Hahahaha. Dude, I don't think I can ride with you.'",
" I was at a restaurant, I saw a guy wearing a leather jacket at the same time he was eating a hamburger and drinking a glass of milk. I said 'Dude, you are a cow. The metamorphosis is complete. Don't fall asleep, I will tip you over.'",
". Seahorses are slow. If I was in the ocean, I would not be a gambler on the horse races ... because you would be there fuckin' days",
" Man, remember that movie The Outsiders and one of the guys name was 'Soda Pop', and at the time it was cool?... It's not cool right now. Your nickname was 'Soda Pop'... you would be dead.",
" I remixed the remix... it was back to normal.",
"As an adult, I'm not supposed to go down slides. So if I end up at the top of a slide, I have to act like I got there accidentally. 'How'd I get up here, god damnit?! I guess I have to slide down.'",
"My manager's cool, he gets concerned, he says, 'Mitch, don't use liquor as a crutch.' I can't use liquor as a crutch... because a crutch helps me walk",
" When I play the South, they say 'y'all'in the South. They take out the 'O' and the 'U'. So when I am in the South, I try to talk like that, so people understand me. 'Hello, can I have a bowl of chicken noodle... sp.'",
" I want to be a race car passenger. Just a guy who bugs the driver.",
" I didn't go to college, but if I did, I would have taken all my tests at a restaurant, because the customer is always right.",
"Alcoholism is a disease. But it's like the only disease you can get yelled at for having. ",
" I was gonna stay overnight at my friends place, he said 'You're gonna have to sleep on the floor.'.... Damn gravity. You got me again. You know how badly I want to sleep on the wall.",
"Dogs are forever in the pushup position.",
"I did comedy for a fundraiser once. We were trying to raise money to buy one of those machines that shows how much money has been raised",
"I saw a commercial for an above ground pool, it was 30 seconds long. You know why? Because that's the maximum amount of time you can depict yourself having fun in an above ground pool.",
"I got a fire alarm at home, but really it's more like a 9-volt battery slowly drainer. 'Do you want to slowly get rid of your 9-volt batteries? Then buy this circle.'",
"You know when they show someone on TV washing their hair under a waterfall? That's fuckin' bullshit, man. Because that thing would knock you on your ass.",
"I'd like to see a forklift lift a crate of forks. It'd be so damn literal! You are using that machine to it's exact purpose!",
" Now if I was to give a duck bread, I'd give him Pepperidge Farm bread because that shit's fancy. It's wrapped twice. So you open it... and it still ain't opened. That's why I don't buy it. I don't need another step between me and toast"];
jokes=list(set(jokes));
stop_words=set(stopwords.words("english"));
filtJokes={};
taggedJokes={}
sList=[];
for i in jokes:
	j=word_tokenize(i);
	sList=[w for w in j if not w in stop_words]
	filtJokes[i]=sList;
#print filtJokes;
train_text=state_union.raw('2005-GWBush.txt');
custom_tagger=PunktSentenceTokenizer(train_text);
test_text=' '.join(jokes);
#print test_text;
jokeTags=custom_tagger.tokenize(test_text);
cnt=1;
for i in jokeTags:
	wds=word_tokenize(i);
	tags=nltk.pos_tag(wds);
	taggedJokes[cnt]=tags;
	chunker=r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?} """;
	chunkParse=nltk.RegexpParser(chunker);
	chunky=chunkParse.parse(tags);
	#print chunky.draw();
	cnt+=1;
#print taggedJokes;
all_words=[];
for w in test_text.split():
	all_words.append(w);
#print all_words;
all_words=nltk.FreqDist(all_words);
#print all_words.most_common(30);
'''
hedBlob=TextBlob(test_text);
cnt=0;
for sentence in hedBlob.sentences:
	print sentence.sentiment.polarity
	cnt+=1;
print cnt;
'''
for i in jokes:
	blob = TextBlob(i, analyzer=PatternAnalyzer())
	print blob.sentiment
print len(jokes)

