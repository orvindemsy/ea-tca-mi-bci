import numpy.linalg as la
import numpy as np

def csp_feat_ver1(XtrainRaw, XtestRaw, ytr, n_filter=3):
    '''
    This used to be named csp_feat_ver5
    Python implementation of MATLAB csp code, this time function will receive EEG trials raw data
    
    Parameter:
    XtrainRaw : train trials, shape of trials x channels x samples
    XtestRaw : test trials, shape of trials x channels x samples
    ytr : the label class of training data, 1D shape of (trials, ), should contain value (0, 1)
    n_filter: number of filter for spatial filter
    
    Return:
    feat_train: csp feature training, shapae of samples x 2*n_filters
    feat_test: csp feature test, shape of samples x 2*n_filters

    '''
    
    # Separating left and right trial
    ids_left = np.argwhere(ytr == 0).ravel()
    ids_right = np.argwhere(ytr == 1).ravel()

    EEG_left = XtrainRaw[ids_left]
    EEG_right = XtrainRaw[ids_right]

    # Covariance of left and right
    cov_left = 0
    for signal in EEG_left:
        cov_left += np.cov(signal, rowvar=True, ddof=1)

    cov_left = cov_left/EEG_left.shape[0]
    
    cov_right = 0
    for signal in EEG_right:
        cov_right += np.cov(signal, rowvar=True, ddof=1)

    cov_right = cov_right/EEG_right.shape[0]
    
    # Imitating eig(cov_right\cov_left) on MATLAB
    mldiv = la.lstsq(cov_right, cov_left, rcond=None)[0]

    # Eigenvector and eigenvalues
    [eigval, eigvec] = la.eig(mldiv)

    # Sort, descending order, eigvec
    ids_dsc = np.argsort(eigval)[::-1]
    eigvec = eigvec[:, ids_dsc]

    # W matrix
    W = np.delete(eigvec, np.s_[n_filter:-n_filter], axis=1)

    # Calculating feature train 
    feat_train = []
    for trial in XtrainRaw:
        X = W.T@trial
        feat_train.append(np.log10(np.diag(X@X.T)/np.trace(X@X.T)) ) 
    
    # Calculating feature test 
    feat_test = []
    for trial in XtestRaw:
        X = W.T@trial
        feat_test.append(np.log10(np.diag(X@X.T)/np.trace(X@X.T)) ) 
    
    return np.array(feat_train), np.array(feat_test)



def csp_feat_no_test(data, n_filter=3, filter_key = None, eeg_key='all_trials'):
    '''
    This used to be named csp_feat_ver3
    Python implementation of MATLAB csp code, the original work is called TLBCI 
    This function is used to convert all trials into csp feature,
    Thus, there isn't splitting into train and test set in this function
    
    Parameter:
    data      : dictionary containing data of each subject EEG signal, y class
    n_filter  : number of spatial filter to compute
    filter_key: name of filter key if the data is stored in data[filter_key][eeg_data]
    eeg_key   : name of key where the eeg_data is stored
    
    Return    :
    csp_features : csp features of all eeg data.
    '''
    
    if filter_key:
        EEG_all = data[filter_key][eeg_key]
        y       = data[filter_key]['y']
    else:
        EEG_all = data[eeg_key]
        y       = data['y']
    
    ids_left = np.argwhere(y == 0).ravel()
    ids_right = np.argwhere(y == 1).ravel()
    
    EEG_left = EEG_all[ids_left]
    EEG_right = EEG_all[ids_right]

    # Covariance of left and right
    cov_left = 0
    for signal in EEG_left:
        cov_left += np.cov(signal, rowvar=True, ddof=1)

    cov_left = cov_left/EEG_left.shape[0]

    cov_right = 0
    for signal in EEG_right:
        cov_right += np.cov(signal, rowvar=True, ddof=1)

    cov_right = cov_right/EEG_right.shape[0]

    mldiv = la.lstsq(cov_right, cov_left, rcond=None)[0]

    # Eigenvector and eigenvalues
    [eigval, eigvec] = la.eig(mldiv)

    # Sort, descending order, eigvec
    ids_dsc = np.argsort(eigval)[::-1]
    eigvec = eigvec[:, ids_dsc]

    # W matrix
    W = np.delete(eigvec, np.s_[n_filter:-n_filter], axis=1)

    # Calculating feature train 
    all_feat = []
    for trial in EEG_all:
        X = W.T@trial
        all_feat.append(np.log10(np.diag(X@X.T)/np.trace(X@X.T)) ) 

    return np.array(all_feat)

def csp_feat_no_test_2(EEG_all, y, n_filter=3):
    '''
    Modification of csp_feat_no_test
    In the previous function the parameter needs to be data stored in certain format
    In this function you can pass raw data and its corresponding y
    
    Parameter:
    EEG_all     : EEG signal, shape of n_trials x n_electrode x n_timepoints
    y           : y class, label of each trial  
    
    Return:
    csp_feature : csp
    '''
    
    EEG_all = EEG_all
    y       = y
    
    ids_left = np.argwhere(y == 0).ravel()
    ids_right = np.argwhere(y == 1).ravel()
    
    EEG_left = EEG_all[ids_left]
    EEG_right = EEG_all[ids_right]

    # Covariance of left and right
    cov_left = 0
    for signal in EEG_left:
        cov_left += np.cov(signal, rowvar=True, ddof=1)

    cov_left = cov_left/EEG_left.shape[0]

    cov_right = 0
    for signal in EEG_right:
        cov_right += np.cov(signal, rowvar=True, ddof=1)

    cov_right = cov_right/EEG_right.shape[0]

    mldiv = la.lstsq(cov_right, cov_left, rcond=None)[0]

    # Eigenvector and eigenvalues
    [eigval, eigvec] = la.eig(mldiv)

    # Sort, descending order, eigvec
    ids_dsc = np.argsort(eigval)[::-1]
    eigvec = eigvec[:, ids_dsc]

    # W matrix
    W = np.delete(eigvec, np.s_[n_filter:-n_filter], axis=1)

    # Calculating feature train 
    all_feat = []
    for trial in EEG_all:
        X = W.T@trial
        all_feat.append(np.log10(np.diag(X@X.T)/np.trace(X@X.T)) ) 

    return np.array(all_feat)