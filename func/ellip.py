from scipy.signal import ellip, lfilter
from scipy.signal import freqs

def ellip_bandpass(lowcut, highcut, fs, order):
    # Create coefficient of filter
    fnyq = fs/2

    lowcut = 0.5/fnyq
    highcut = 30/fnyq
    
    b, a = ellip(N=order, rp=1, rs=10, Wn=[lowcut, highcut], btype='bandpass')
    
    return b, a

def apply_ellip_bandpass(data, lowcut, highcut, fs, order=4):
    '''
    Parameter:
    data    : data of signal, with shape N x S
    lowcut  : low frequency band of bandpass
    highcut : high freqeuncy band of bandpass
    fs      : frequency sampling
    order   : filter order
    
    N: no. of electrodes
    S: sample, time-series data
    '''
        
    b, a  = ellip_bandpass(lowcut=lowcut, highcut=highcut, fs=fs, order=order)
    
    # Applying filter
    y = lfilter(b, a, data, axis=-1)
    
    return y