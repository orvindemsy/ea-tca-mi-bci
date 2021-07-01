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
<img src="/image/blog-tcadim-acc.png" width="500">
The boldfaced numbers indicate highest accuracy in each method. The results suggest that for all methods, low dimensions (1 or 2) are unlikely to be a good representation of latent space between subjects, while higher dimensions (greater than 3) show better results. In the subsequent evaluation, TCA dimension of 4 is chosen.


### TCA and SVM Kernels vs Accuracy
<!-- ![ker-acc](/image/blog-ker-acc.png) -->
<img src="/image/blog-ker-acc.png" width="700">
This evaluation is done only on the four methods that use TCA. It can be seen that for TCA and EA-TCA, both combinations of linear and radial basis function (rbf) kernel for TCA and SVM do not significantly affect accuracies. On the other hand, for TCA-W and EA-TCA-W, using rbf as SVM kernel can drop accuracies to approximately 50%.

### Number of Source Trials vs Accuracy
<img src="/image/blog-src-acc.png" width="700">
Results suggest that mean accuracy of each method is relatively stable after approximately greater than 30 source trials are used, which implies that even with few source trials, satisfactory classification accuracy can be achieved, especially for methods with EA

### Comparison of All Methods
![eval-all](/image/blog-eval-all.png)

The results suggest that:
- Conventional TCA and proposed TCA-W outperforms baseline be 3.23% and 4.23% respectively.
- Applying EA to both TCA improves performance. EA-TCA outperforms TCA by 5.61% and EA-TCA-W outperforms TCA-W by 6.79%.
- In general methods with EA generally performs better than those without EA.
- Preliminary experiment shows that for 20 repititions, proposed TCA-W can speed up processing time by 52% compared to conventional TCA.