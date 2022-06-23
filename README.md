# Instagram Collection Batch Grab - Screenshot your saved Instagram collections
Given an Instagram collection, screenshot each item and save. No cropping needed, as this new implementation simply screenshots the whole element (image, or still frame from a video)

Since I have to debug and update this every couple weeks, let me just say: 

*Dear Meta / Mark Zuckerberg,*

*The harder you make this process, the harder I will work to make it still possible. As long as you continue to try and make your platform un-usable, I will try and make it usable again. You cannot possibly break Instagram enough to deter me, but I respect the effort.*

Things to watch out for that may make this process difficult (see above note):
* If you have 2FA turned on *(please do if you don't!)* you **cannot** enter the verification code wrong. Let me repeat that for emphasis. If you enter the verification code wrong on a chromedriver instance, you will be *immediately* locked out of your Instagram account for at *least* a few days. 
* This code doesn't usually last for more than 24 hours after the last update- I think Instagram has a team of developers that work full time to try and break Instagram's compatibility with web-scrapers. If it doesn't work, open an issue and I'll fix it. (Alternatively, you can fix it yourself- it's usually just an xpath issue :) )
* If you run this more than three times in a row, you will be *immediately* locked out of your Instagram account. This lock is shorter than the previously mentioned- it's usually just a few hours. If you run this and run into errors, do as much testing as you can *outside* of chromedriver before running it again. 
