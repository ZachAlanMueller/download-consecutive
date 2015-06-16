import urllib, urllib2, sys, time

podNumber = 307


def main():
    global podNumber

    beg = "http://www.podtrac.com/pts/redirect.mp3/traffic.libsyn.com/rtpodcast/Rooster_Teeth_Podcast_"
    mid = str(podNumber)
    end = ".mp3"
    downURL = beg + mid + end
    downURLName = "RT Podcast #" + str(podNumber)
    folder = "Podcasts/"


    try:

        print "Downloading "+ downURLName
        print "Download in progress.."


        urllib.urlretrieve (downURL, folder + downURLName)



        podNumber = podNumber + 1
    except:
        print "Error detected"
        sys.exit()


while podNumber <= 327:
    main()
