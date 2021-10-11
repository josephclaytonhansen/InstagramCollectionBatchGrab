# Instagram Collection Batch Grab
Given an Instagram collection, screenshot each item and crop down to picture/caption

## Example Output
![cropped screenshot](https://github.com/josephclaytonhansen/InstagramCollectionBatchGrab/blob/main/00165.png)

## Usage
Change the 'start_url' in grab.py to the correct URL. Run the script and log in to Instagram (not worth automating this step). Once you're logged in, type anything in response to the "Logged in?" prompt and hit Enter. The script will now take a screenshot of every image in the collection. This may take a while- because Instagram loads in "chunks", and it's very difficult to tell when that loading will be triggered, I had to use a delay of 3 seconds between each image. You can change this if you have faster or slower internet. 

Once this is done, run "crop.rb" in the directory. Make sure you have a "/cropped" subdirectory. You'll need MiniMagick installed. 
