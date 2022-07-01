"""
binarysearch.com :: Circular Longest Increasing Subsequence
jramaswami
"""


import bisect
import collections
import math


class Solution:
    def solve(self, nums):
        def lis(A):
            T = [math.inf for _ in A]
            T[0] = math.inf
            for n in A:
                # Find the left index of the first element greater than or
                # equal to n
                i = bisect.bisect_left(T, n)
                T[i] = n
            return bisect.bisect_left(T, math.inf)

        soln = 0
        Q = collections.deque(nums)
        for _ in nums:
            soln = max(soln, lis(Q))
            Q.rotate(-1)
        return soln


def test_1():
    nums = [5, 4, 7, 1, 2, 3]
    expected = 5
    assert Solution().solve(nums) == expected


def test_2():
    nums = [-641, 48, -7, -164, -172, 245, 341, -932, -742, -744, 312, -212, -600, 323, -363, 240, 57, -656, 642, 203, -333, -262, 826, 90, 334, -355, 978, -51, 847, -221, 366, -15, -506, 784, -147, 893, 749, -527, -497, -61, 364, -581, -186, -152, -361, 864, -684, -776, 627, -301, -538, 369, -864, 36, 201, 164, -833, 737, -901, 380, -514, 484, 882, 609, 776, 333, 912, 199, 829, -59, 181, -623, -976, 893, 957, 297, -841, -182, 445, -665, 898, 129, 664, -874, 73, 658, 196, -271, -7, 428, 15, -996, -564, 705, -344, 93, 507, -544, 495, -193, 156, -239, 280, 815, -575, -533, -693, -199, -361, -52, 636, -723, 712, 636, 951, 444, 759, 28, 93, -553, -396, 132, 404, -900, -913, 273, -10, 144, 241, -838, -911, 675, -869, -350, 122, -899, 45, 697, -423, -116, 723, 893, 556, 432, 737, -469, -629, 266, 134, -481, 751, -796, -234, 862, -802, 144, 451, -525, -212, -966, -196, -554, -269, 968, -517, 967, -503, 715, 176, 275, -869, 396, -582, 103, -200, -62, 50, 598, 888, 715, 848, -944, 853, 183, -517, 241, 824, 466, -448, 607, -497, -785, -5, -467, 375, 911, -758, -60, -641, 404, -734, 165, -784, -303, 859, -249, -340, -132, -379, -116, -346, -247, 52, -317, 909, 718, -839, -20, -235, 740, -819, -802, -93, 524, -649, -828, -518, -449, 560, 346, -505, 659, -573, 195, -69, 656, -145, 48, 884, -442, -572, -99, -180, 29, -947, 951, 872, -870, -592, 1, 951, -762, 5, -390, 632, -622, -101, -905, -200, -394, -673, 808, 701, -344, -903, -24, -677, 868, 649, 643, 537, 159, 947, -987, -5, 593, 779, 804, 486, 56, 24, -770, 663, 845, 381, 342, 248, 950, 743, -159, -480, -766, -367, -982, -605, 88, -718, -807, -120, 434, 981, 742, -226, -713, -216, -598, 826, -550, -84, 425, 757, -897, -192, -425, -360, -773, 100, 804, 86, -905, 352, -553, -971, -456, 925, -108, -617, -376, -713, 212, -129, -17, -550, 53, 141, 639, -254, 425, 277, -872, -366, 145, -549, 397, -633, 99, 474, 438, -818, 776, -972, 192, 740, -365, 241, 103, 579, -588, 556, 495, 15, 653, 647, -587, -134, 717, -745, -963, 394, -329, 637, -524, -976, -904, 874, -538, 343, -858, 821, 76, 884, -982, -75, 694, -1000, -441, -312, 48, 420, 22, 471, 509, -302, 225, -564, -36, -168, -24, 985, -662, -792, 834, -746, 508, 73, 149, -541, 871, -761, -743, 867, -599, 6, -997, -370, 113, 445, -495, -41, -270, -708, -348, -975, -751, -622, 862, -970, -356, -133, -720, -644, 336, 139, 956, 56, -318, 660, -267, 892, 130, 109, 359, -345, -775, 9, -760, -596, -544, 965, 548, 670, 594, -639, -290, -740, -872, -133, 126, -14, -882, 920, -105, -636, -431, -25, -786, -804, -435, 431, 334, 882, 547, -136, 860, -902, -487, -762, -520, 620, -252, 945, -337, 18, 528, -868, 446, -126, 420, 957, -818, 837, 929, -79, 129, -321, -649, -545, 245, -490, -641, -264, -301, -620, 407, -498, -388, 230, -465, -779, 400, -175, 515, -174, -818, -459, -860, -68, -87, -435, -802, -887, -183, -759, 133, 289, 431, 390, -381, -14, 871, -79, 663, -351, 498, 292, 785, 563, 275, -66, 616, -905, 485, 465, 623, 693, -203, 371, 44, 682, -609, 662, 386, -528, 585, 141, 927, -929, -561, 639, 192, -548, -754, 413, -7, -927, 232, -557, -895, -934, 901, -51, -65, 300, 36, 344, -565, 961, -687, -228, 159, 188, 193, 312, -226, -517, -335, -996, -771, -868, -682, -881, 337, 412, 174, -860, -643, -68, 534, 799, 114, -87, -594, -139, 649, 245, 536, 66, 994, 755, -642, -143, -817, -626, -680, -294, -677, -876, 523, -692, -233, -141, 812, 749, 790, -87, 3, 446, -418, -336, 890, 226, -384, 922, 834, -426, 711, 314, -92, -955, -942, 316, -74, 471, -280, -217, -145, 963, 163, 584, 996, -820, -212, 179, -30, -681, -806, 984, -797, 242, -968, -733, 146, -280, -71, -18, 87, -995, 156, -683, -253, -522, 902, 105, 534, 913, -9, 181, -177, 134, -304, -480, -233, 718, 17, 212, -327, 503, 313, 518, 872, 680, -950, -484, -350, -865, -244, 539, -870, -757, -456, -325, 700, -831, -123, -550, 787, 261, -52, 327, 242, 867, 139, -271, -846, 511, 861, 99, 474, -696, 192, 291, 431, -139, -947, 969, 216, 276, 569, 390, 954, -635, 206, 497, -655, 109, -183, -815, -679, -435, 699, 518, -886, 165, -738, -104, 483, -946, -172, 162, 897, -479, 324, 810, -877, -469, 940, -330, -462, 967, 634, -216, 536, -888, 720, 107, -299, 599, 239, 511, 636, -622, 431, 747, 270, 732, 621, -293, 343, -826, -782, -706, 708, 729, -89, 373, -660, 501, -370, 20, -740, 277, 979, 630, 22, 457, 451, -399, 797, -778, -730, 667, -83, 314, 564, -484, -835, -261, 289, -997, -392, -173, -647, 27, -281, 732, -430, -747, 955, 916, -997, 50, -277, 823, 953, -39, -865, -882, 470, 371, 537, 663, -314, 316, 676, -368, -450, 429, -91, 766, -293, 596, 298, -530, 863, 103, 252, 842, 303, -505, -172, 212, 298, -383, -432, 934, -631, 313, -710, 729, -848, 592, 415, -867, -778, 941, -945, -535, -874, -920, -515, 201, -687, -922, -854, 456, 745, 424, -919, -135, 798, -442, -57, 393, -711, 439, -841, -191, 556, -23, 972, -655, 687, -979, -726, 989, 1, 375, -62, 341, -916, -921, 343, 46, 565, 432, -716, -864, 489, 145, 873, -600, 316, 667, 362, 43, -468, 974, 702, -265, 333, 494, -688, -38, 115, -55, 603, 292, -956, -330, 607, 201, 170, -297, -928, 827, -688, 80, 68, -388, -27, -885, -718, -958, 934, -596, -794, -441, 855, 189, 164, 718, -401, 857, 322, 570, 585, 729, -279, -858, -780, -544, 893, 713, -254, -409, -533, -776, 44, 313, 542, 215, 167, -325, -710, 968, -368, 488, 800, -879, -742, -35, -893, 442, 633, 460, 130, -598, 892, 399, -114, -187, -639, 382, -504, -327, 817, 608, 523, 325, 968]
    expected = 62
    assert Solution().solve(nums) == expected