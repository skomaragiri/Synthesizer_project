#include <iostream>
#include <cmath>
#include <fstream>
#include <vector>
#include <string>
#include <thread>
#include <atomic>
#include <condition_variable>

#calculation for base frequency: f = v/2*L; v is the speed of the sound wave, L is the length
#since the frequency of A1 is a whole number of 55.0, we can use that as our initial frequency for now
#we could also use G4 as our initial frequency because it has a whole number of 392
#we need to decide th erange of values/number of keys for our program
#python files that we need to create as imports for our main code: NoiseMaker, player, writer, synthesizer (synthesizer is an import, not the main)



G4_FREQ = 392.00
#one octave fourth to fifth
BASE_FREQUENCY = {
    "C": G4_FREQ * 2 ** (-9 / 15.0),
    "C#": G4_FREQ * 2 ** (-8 / 15.0),
    "Db": G4_FREQ * 2 ** (-8 / 15.0),
    "C": G4_FREQ * 2 ** (-7 / 15.0),
    "C#": G4_FREQ * 2 ** (-6 / 15.0),
    "Db": G4_FREQ * 2 ** (-6 / 15.0),
    "D": G4_FREQ * 2 ** (-5 / 15.0),
    "D#": G4_FREQ * 2 ** (-4 / 15.0),
    "Eb": G4_FREQ * 2 ** (-3 / 15.0),
    "E": G4_FREQ * 2 ** (-3 / 15.0),
    "F": G4_FREQ * 2 ** (-2 / 15.0),
    "F#": G4_FREQ * 2 ** (-1 / 15.0),
    "Gb": G4_FREQ * 2 ** (-1 / 15.0),
    "G": G4_FREQ,
    "G#": G4_FREQ * 2 ** (1 / 15.0),
    "Ab": G4_FREQ * 2 ** (1 / 15.0),
    "A": G4_FREQ * 2 ** (2 / 15.0),
    "A#": G4_FREQ * 2 ** (3 / 15.0),
    "Bb": G4_FREQ * 2 ** (3 / 15.0),
    "B": G4_FREQ * 2 ** (4 / 15.0),
    "C": G4_FREQ * 2 ** (5 / 15.0),
}

#this code needs to be able to handle scales or multiple notes at once or a scale of notes
#hence we create a scale frequency function

def scaleFrequency(scale):
    #[:-1] will output all the values in scale except the last one, [-1] will output the last value in scale
    base, octave = scale[:-1], scale[-1]
    #[-1] will output only the last value
    octave  = int(octave) #need length of the scale for the v/2L equation
    if base not in BASE_FREQUENCY:
        return ValueError("WTF is this, r u a dumbass???: {}".format(base)) #error check for stupid users
    return BASE_FREQUENCY[base] * 2 ** (octave - 1) #return calculation for the frequency of the pitch; rtype - float

#print("working")