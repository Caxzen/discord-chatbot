import random
import discord 
from discord_buttons_plugin import *
from discord.ext import commands,tasks
import requests


reaction_hug = ["https://acegif.com/wp-content/gif/anime-hug-38.gif",
"https://acegif.com/wp-content/gif/anime-hug-59.gif",
"https://acegif.com/wp-content/gif/anime-hug-49.gif",
"https://acegif.com/wp-content/gif/anime-hug-86.gif",
"https://acegif.com/wp-content/gif/anime-hug-79.gif",
"https://acegif.com/wp-content/gif/anime-hug-79.gif",
"https://acegif.com/wp-content/gif/anime-hug-50.gif",
"https://acegif.com/wp-content/gif/anime-hug-83.gif",
"https://acegif.com/wp-content/gif/anime-hug-14.gif",
"https://acegif.com/wp-content/gif/anime-hug-63.gif",
"https://acegif.com/wp-content/gif/anime-hug-27.gif",
"https://acegif.com/wp-content/gif/anime-hug-73.gif",
"https://acegif.com/wp-content/gif/anime-hug-75.gif",
"https://acegif.com/wp-content/gif/anime-hug-10.gif",
"https://acegif.com/wp-content/gif/anime-hug-22.gif"]
reaction_kiss = ["https://acegif.com/wp-content/uploads/anime-kissin-2.gif",
"https://acegif.com/wp-content/uploads/anime-kissin-16.gif",
"https://acegif.com/wp-content/uploads/anime-kissin-1.gif",
"https://acegif.com/wp-content/uploads/anime-kissin-3.gif",
"https://acegif.com/wp-content/uploads/anime-kissin-5.gif",
"https://acegif.com/wp-content/uploads/anime-kissin-8.gif",
"https://acegif.com/wp-content/uploads/anime-kiss-38.gif",
"https://acegif.com/wp-content/uploads/anime-kiss-32.gif",
"https://acegif.com/wp-content/uploads/anime-kiss-17.gif",
"https://acegif.com/wp-content/uploads/anime-kiss-6.gif",
"https://acegif.com/wp-content/uploads/anime-kiss-11.gif",
"https://acegif.com/wp-content/uploads/anime-kiss-11.gif",
"https://acegif.com/wp-content/uploads/anime-kiss-7.gif",
"https://acegif.com/wp-content/uploads/anime-kiss-1.gif",
"https://acegif.com/wp-content/uploads/anime-kiss-25.gif"]
reaction_bite = ["https://i.imgur.com/0d1y9zF.gif",
"https://i.imgur.com/1EtOphf.gif",
"https://i.imgur.com/rSYvWUg.gif",
"https://i.imgur.com/dqsYXOL.gif",
"https://i.imgur.com/FlwJbPh.gif",
"https://i.imgur.com/kUEaRIu.gif",
"https://i.imgur.com/VKgFBJY.gif",
"https://i.imgur.com/r9QOkEA.gif",
"https://i.imgur.com/f4MAKp8.gif",
"https://i.imgur.com/2K66vgG.gif",
"https://i.imgur.com/ffkBusx.gif"]
reaction_slap = ["http://i.imgur.com/iekwz4h.gif",
"http://i.imgur.com/DvwnC0r.gif",
"http://i.imgur.com/d9thUdx.gif",
"http://i.imgur.com/b75B4qM.gif",
"http://i.imgur.com/CHbRGnV.gif",
"http://i.imgur.com/rk8eqnt.gif",
"http://i.imgur.com/Ksy8dvd.gif"]
reaction_poke = ["http://i.imgur.com/urC9B1H.gif",
"http://i.imgur.com/TzD1Ngz.gif",
"http://i.imgur.com/3kerpju.gif",
"http://i.imgur.com/bStOFsM.gif",
"http://i.imgur.com/uMBRFjX.gif",
"http://i.imgur.com/1PBeB9H.gif",
"http://i.imgur.com/dfoxby7.gif",
"http://i.imgur.com/YDJFoBV.gif",
"http://i.imgur.com/i1hwvQu.gif"]
reaction_pat = ["http://i.imgur.com/75FpUOd.gif",
"http://i.imgur.com/Cju6UX3.gif",
"http://i.imgur.com/UwcwNiU.gif",
"http://i.imgur.com/FAHxGpn.gif",
"http://i.imgur.com/SuU9WQV.gif",
"http://i.imgur.com/VuucXay.gif",
"http://i.imgur.com/QxZjpbV.gif",
"http://i.imgur.com/SpoJHzQ.gif",
"http://i.imgur.com/7wZ6s5M.gif",
"http://i.imgur.com/pnb1k5P.gif",
"http://i.imgur.com/rMeGX0k.gif",
"http://i.imgur.com/0FLNsZX.gif",
"http://i.imgur.com/4SiEFQq.gif",
"http://i.imgur.com/4GgbYst.gif",
"http://i.imgur.com/1mr4NWL.gif",
"http://i.imgur.com/V2VFPSj.gif",
"http://i.imgur.com/b2dC2pu.gif",
"http://i.imgur.com/ZCucIDe.gif",
"http://i.imgur.com/bOrLVXd.gif",
"http://i.imgur.com/Y2DrXtT.gif",
"http://i.imgur.com/nsiyoRQ.gif",
"http://i.imgur.com/JjWLlcz.gif"]
reaction_cry = ["http://i.imgur.com/NkLgdj8.gif",
"http://i.imgur.com/2HPoWSf.gif",
"http://i.imgur.com/7Tw9dPP.gif",
"http://i.imgur.com/7Tw9dPP.gif",
"http://i.imgur.com/YANiZ2a.gif",
"http://i.imgur.com/3zVAY49.gif",
"http://i.imgur.com/SalWtcC.gif",
"http://i.imgur.com/kysvK28.gif",
"http://i.imgur.com/WLNfW3d.gif",
"http://i.imgur.com/DhkvnpB.gif",
"http://i.imgur.com/sYV2GBp.gif",
"http://i.imgur.com/rmlZXaP.gif",
"http://i.imgur.com/5vUBsz4.gif",
"http://i.imgur.com/mvyAx5q.gif",
"http://i.imgur.com/ekhYSVB.gif",
"http://i.imgur.com/nE0Tdp0.gif",
"http://i.imgur.com/sYV2GBp.gif",
"http://i.imgur.com/RXdJczP.gif",
"http://i.imgur.com/qfcReCj.gif"]
reaction_cuddle = ["http://i.imgur.com/K4lYduH.gif",
"http://i.imgur.com/Asnv32U.gif",
"http://i.imgur.com/8kLQ55E.gif",
"http://i.imgur.com/Asnv32U.gif",
"http://i.imgur.com/kd0F5bV.gif",
"http://i.imgur.com/ct76LIg.gif"]

tod_truth = ["What is the most embarrassing thing you’ve ever done?",
"What is the meanest thing you’ve ever done to somebody?",
"Have you ever peed yourself as an adult or teenager?",
"What is something illegal you’ve done?",
" What is the grossest thing you’ve overheard someone do?",
"Tell me something you don’t like about me.",
"Who is a person you don’t like but pretend to?",
"Who is one person you wish was still in your life?",
"Do you think you’re uglier or better looking than most people you know?",
"What is the silliest thing you’re genuinely scared of?",
"If you were able to live to the age of 90 and retain either the mind or body of a 30-year-old for the last 60 years of your life, which would you want?",
"For what in your life do you feel most grateful?",
"Who in the group do you think will end up the richest?",
"If you could wake up tomorrow having gained any one quality or ability, what would it be?",
"Would you want to be famous? In what way?",
"What would be a perfect day for you?",
"What is your guilty pleasure?",
"If you knew that in one year you would die suddenly, would you change anything about the way you are now living? Why?",
"What's your most self-destructive behavior?",
"What is the greatest accomplishment of your life?",
"If a crystal ball could tell you the truth about yourself, your life, the future or anything else, what would you want to know?",
"How close is your family? Do you feel your childhood was happier than most other people's?",
"What do you value most in a friendship?",
"What's a useless piece of knowledge that you know?",
"What is your most treasured memory?",
"If you could change anything about the way you were raised, what would it be?",
"What would you do if you switched genders for a day?",
"When did you last cry in front of another person? By yourself?",
"Have you ever been pulled over by the cops?",
"Have you ever catfished anybody? If so, what happened? If not, have you wanted to?",
"What is the naughtiest thing you’ve ever done?",
"What is the biggest lie you’ve ever told, and who did you tell it to?",
"If you had to hook up with one family member, who would it be?",
"What would you buy me if I gave you $50?",
"Who do you hate and why?",
"If you suddenly became invisible what would you do?",
"If you had to kiss a Disney character, who would you choose?",
"What is the last thing that made you cry?",
"Who is the last person you tried to impress?",
"What’s your deepest secret?",
"What do you like most about the person asking you this question?",
"Have you ever cheated on a test?",
"What do you find the most attractive in a person?",
"What do you find the least attractive in a person?",
"What would you do if you were the opposite sex for a month?",
"What are some things you think about when you are sitting on the toilet?",
"Do you pee in the shower?",
"Name three things you and the question asker appear to have in common.",
"What is the most embarrassing thing that your parents have caught you doing?",
"When was the most inappropriate time that you farted?"
]

tod_truth18 = ["Who are you crushing on right now?",
"How many people have you kissed or slept with?",
" Tell me a time you were rejected, and describe it in detail for at least five minutes!",
"If you had to go out on a date with one person of the same s*x, who would it be?",
"Describe what your crush looks like",
"Why did you break up with your last boyfriend or girlfriend?",
"Who have you loved, but they didn’t love you back?",
"What is your greatest fear in a relationship?",
"What is the weirdest thing you have done for a boyfriend or girlfriend?",
"Have you ever gotten really drunk and done anything silly?",
"Have you ever walked in on your parents having sex?",
"What are your top three turn-ons?",
"Which famous married couple would you like to have a threesome with?",
"Describe your most recent romantic encounter.",
"What is your biggest sexual fantasy?",
"How old were you when you first masturbated?",
"Would you ever date two people at once if you could get away with it?",
"Have you ever sent someone a nude?",
"Have you ever received nudes?",
"What color and kind of underwear are you wearing right now?",
"What do you value most in a relationship?",
"Are you sexually attracted to anyone in the group?",
"Would you ever sleep with your ex's best friend?",
"What is the biggest turn off in a partner?",
"What's the most romantic thing you've ever done?",
"What do you wear to bed when you are in the mood?",
"Do you like sexting?",
"Have you ever been in a friends with benefits situation?",
"What is the difference to you between sex and making love?",
"What's your #1 sex jam?",
"What is the weirdest thing you dreamt of doing with a girl/boy?",
"Who in the group would be the hottest in 15 years?",
"Have you ever had a one night stand?",
"What is your idea of perfect foreplay?",
"Which of us do you think has had sex most recently?",
"What is your opinion on love bites, do you want to give me any?",
"What part of your body do you enjoy the most on a women/men?",
"Describe your idea of a perfect date.",
"Do you think you'd be a good parent?",
"If you had to choose between dating someone ugly who was good in bed or dating someone hot who was bad in bed, which would you choose?",
"Are you a virgin?",
"Would you rather have sex with someone 20 years older or 20 years younger?",
"Do you remember the first time you experienced an orgasm? Tell us about it.",
"What’s your favorite body part on your body?",
"Have you ever been tempted to cheat on your significant other?",
"What’s your favorite position?",
"Do you think virginity is special?",
"Do you prefer sex when you’re in love or when it’s a hot hookup?",
"Who in the room do you think has slept with the most people?",
"What fictional character have you or could you have sexual fantasies about?",
"Would you rather be the person doing the spanking or be spanked yourself?",
"What’s a position you want to try?",
"How often do you pleasure yourself a week?",
"Tell me about the best orgasm you’ve ever had.",
"Would you rather give or receive pleasure?",
"Do you like sex to be rough or sensual?",
"Where is your favorite place to be kissed on your body?",
"If I went through your room, would I find anything hidden or interesting?",
"Do you have a name for your penis or vagina?",
"What’s the hottest body part on a girl?",
"What’s the hottest body part on a guy?",
"How often do you shave down there?",
"Which celebrity would you do in an instant if you had the chance?",
"Do you save nudes from old hookups or exes?",
"Have you ever had sex with a MILF? If not, do you want to?",
"If you were going to have a threesome, would you want the third party to be another girl or a guy?"
]

tod_dare = ["Mix a drop of every condiment in your house and drink/eat it.",
"Message someone you haven’t talked to in at least 1 year on Facebook or Instagram and take a screenshot.",
"Do a three-way prank call to somebody so I can listen.",
"Send me a screenshot of your messages with the last person besides me you texted.",
"Text a random number a selfie.",
"Use a picture of me as your phone background for 3 days",
"Screen share your search history from today.",
"Show the group your best dance move.",
"Show the group the insides of your closet.",
"Call someone and confess your new love of Justin Beiber",
"Do your best impersonation of the question asker or someone in the group.",
"Show the group an embarrassing photo from your childhood.",
"Write a status on Discord praising me",
"Take a video of yourself drinking water like a dog",
"Try to lick your elbow.",
"Howl like a dog for one minute.",
"Eat a whole piece of paper.",
"Share the most recent photo on your phone with the group.",
"Spin around 10 times and try to walk straight.",
"Invite anyone in the group's choosing to join the call.",
"Post an embarrassing photo on your Instagram story.",
"Fill your mouth with water and act as a fountain.",
"Draw something on your face with marker.",
"Send me the ugliest selfie you have on your phone."
]

tod_dare18 = ["Text your crush and ask them out on a date.",
"Put ice cubes down your pants and try to shake them out and send me a video.",
"Cut a piece of your hair.",
"Share the most recent photo on your phone with the group.",
"Screen share your search history from today.",
"Show the group an embarrassing photo from your childhood.",
"Watch five minutes of an adult movie I’ll send you.",
"Text a random number and write “I see dicks flying”.",
"Write a break-up text message and send it to someone random in your contacts. Take a screenshot",
"Call a stranger and tell them a secret",
"Post an embarrassing photo on your Instagram story.",
"Color one of your front teeth black and take a selfie",
"Text your recent chat a picture of your toe.",
"Seductively eat a banana.",
"Spit or swallow?",
"Call a relative. The group can ask one question.",
"Share a spicy photo with the group.",
"Whisper someone in the group’s name in a seductive way.",
"Read lyrics “Baby” by Justin Bieber to the group in your most seductive voice.",
"Change your clothing in front of the group.",
"Do a blowjob using a banana or other similar object.",
"Take off one of a clothing.",
"Call your mom and tell her you can’t find a boyfriend/girlfriend in a panicked voice",
"Pole dance with an imaginary pole.",
"Show the group the insides of your closet.",
"Send a sexy text to the 20th person in your contact list.",
"Send a Snapchat to your ex.",
"Play “fuck, marry, kill” with three people in the room.",
"Message something bold to someone hot you’ve been wanting to get to know",
"Fake your best orgasm in front of the group.",
"Prank call someone and pretend to be a sex ad.",
"Send a dirty text in emojis to someone that they have to figure out.",
"Send me a photo of your sexiest pair of underwear.",
"Call your partner and have them quiz you on basic math or trivia for a minute while you watch porn. Let’s see how good you do!",
"Put someone’s underwear on your head.",
"Fake an orgasm for 10 seconds.",
"Try to pick up someone in the room.",
"Lick the floor.",
"Show us your go-to porn video.",
"Beg someone to do naughty things to you. It better be convincing!",
"Spank yourself while calling yourself a “bad boy” for 20 seconds."
]

