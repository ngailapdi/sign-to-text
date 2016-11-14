# MagicHand - Translating sign language to audio

This project is made during HackGSU 2016 and was awarded "Hackathon Winner - Organizer's Choice'

Link to Devpost: https://devpost.com/software/magichand

MagicHand helps translate sign language (by images) to voice in any language using K-Nearest Neighbors algorithms in OpenCV

### Installation
MagicHand requires [OpenCV 2.x](http://#) and [Python 2.7](https://www.python.org/download/releases/2.7/)


First of all we'll be using the package manager Homebrew to simplify things. You can get it here: http://brew.sh/

Once you have brew installed you can go ahead and and add homebrew/science which is where OpenCV is located using:

```sh
$ brew tap homebrew/science
```
Go ahead and install OpenCV now

```sh
brew install opencv
```
You’re done! You can find OpenCV at

```sh
cd /usr/local/Cellar/opencv/2.x.x/
```

Python Setup:

Navigate to your python path, you can find it in your .bash_profile or using

```sh
cat ~/.bash_profile | grep PYTHONPATH
```

Your .bash_profile might not have the PYTHONPATH. In that case, it's dependent on each computer. For my Mac, it was:

```sh
cd /Library/Python/2.7/site-packages/
```

Once there we need to link our compiled OpenCV files, create a symlink using

```sh
$ ln -s /usr/local/Cellar/opencv/2.x.x/lib/python2.x/site-packages/cv.py cv.py
$ ln -s /usr/local/Cellar/opencv/2.x.x/lib/python2.x/site-packages/cv2.so cv2.so
```

### Usage

* This program has been tested on Mac. os.say() will not work in Windows OS. You will need to modify os.say() to a similar window cmd in order for it to work
* Run train.py to train the data set for your hand gesture (you can only map **numbers** to the gestures, NOT characters.
* Map the number with associated words/phrases by modifying the words dict in main.py
* Run main.py to detect and say the gesture you've already mapped
```python
words = {0: 'Hello', 1: 'I', 2: 'Love', 3: 'You', 5: 'Good Bye', 7: 'Hack GSU 2016'}
```

## Contributors

This project is made by VNBuzz - 4 Georgia Tech students: 
* [Sim Kieu](https://github.com/simkieu)
* [Vinh Tran](https://github.com/daivinhtran)
* [Khoa Ho](https://github.com/dangkhoa141)
* [Anh Thai](https://github.com/ngailapdi)
