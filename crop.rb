require "mini_magick"

def crop(path, thres)
    image = MiniMagick::Image.open(path)
    image.combine_options do |c|
        c.crop "75%x75%+0+100"
        c.fuzz thres
        c.trim "+repage"
        c.write("cropped/"+path)
    end
end

l = Dir.glob("*")
l.delete("cropped")
l.delete('crop.rb')
l.each do |n|
    crop(n, "42%")
end
