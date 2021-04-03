from scipy.signal import butter, lfilter
from scipy.signal import freqs

def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = fs/2
    low = lowcut/nyq
    high = highcut/nyq
    b, a = butter(order, [low, high], btype="band")
    
    return b, a

def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    '''
    Parameter:
    data   : array containing eeg data, shape of (n_electrode x samples)
    lowcut : lowcut frequency, integer 
    highcut: highcut frequency, integer
    fs     : frequency sampling, integer
    order  : order of butterworth filter
    
    '''
    
    b, a = butter_bandpass(lowcut, highcut, fs=fs, order=order)
    y = lfilter(b, a, data, axis=-1)
    
    return y