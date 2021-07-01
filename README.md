# Transfer Learning Using EA and TCA for MI-BCI
Master's degree final research project.

## Abstract/Overview
*Abstract*—Brain-computer interface (BCI) requires calibration phase to learn user-specific decoder that translates brain signals into desired commands. Calibration phase can be lengthy and exhausting for motor imagery-based (MI) BCI, and can potentially reduce the effectiveness of BCI system. Transfer learning (TL) approaches have been implemented in the field of BCI to tackle
this problem. Transfer learning based on domain adaptation reduces domain discrepancy between two domains. Transfer component analysis (TCA) is one domain adaptation technique that maps features of both domains into a new space while simultaneously reducing their domain discrepancy. Recently,
Euclidean alignment (EA) is used as transfer learning technique in BCI preprocessing step to align electroencephalography (EEG) trials between subjects. This paper proposed a combination of both EA and TCA (EA-TCA) as a TL approach for inter-subject transfer learning. This paper also proposed TCA method that can reuse existing projection matrix to transform new target data (TCA-W). The efficacy of EA to this method is also observed
(EA-TCA-W). Results indicate that EA-TCA and EA-TCA-W outperform classification accuracy of those without EA by 5.61% and 5.79%, respectively. This concludes that EA can improve performance of both conventional TCA and proposed TCA-W.

## Result Overview
### TCA dimension vs Accuracy
<!-- ![ker-acc](/image/blog-tcadim-acc.png) -->
<img src="/image/blog-tcadim-acc.png" width="350">

### TCA and SVM Kernels vs Accuracy
![ker-acc](/image/blog-ker-acc.png)

### Number of Source Trials vs Accuracy
![src-acc](/image/blog-src-acc.png)


### Comparison of All Methods
![eval-all](/image/blog-eval-all.png)
