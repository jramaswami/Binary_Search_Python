"""
binarysearch.com :: Update List Sum Closest to Target
jramaswami
"""


import bisect
import itertools


class Solution:

    def solve(self, nums, target):
        nums.sort()
        prefix = list(itertools.accumulate(nums))

        def compute_sum(e):
            "Return sum of nums if all num[i] > e are replaced with e."
            i = bisect.bisect_right(nums, e)
            if i == 0:
                return len(nums) * e
            elif i < len(nums):
                return prefix[i-1] + (e * len(nums) - i)
            else:
                return prefix[-1]

        lo = 0
        hi = nums[-1]
        delta = target
        soln = target
        while lo <= hi:
            e = lo + ((hi - lo) // 2)
            t = compute_sum(e)
            d = abs(target - t)
            if d < delta:
                delta = d
                soln = e
            if t < target:
                # try larger
                lo = e + 1
            elif t > target:
                # try smaller
                hi = e - 1
            else:
                return e
        return soln


def test_1():
    nums = [2, 4, 3, 7, 7, 1]
    target = 10
    expected = 2
    assert Solution().solve(nums, target) == expected


def test_2():
    nums = [3, 3, 3]
    target = 100
    expected = 3
    assert Solution().solve(nums, target) == expected


def test_3():
    nums = [929, 255, 285, 300, 175, 256, 917, 722, 494, 415, 370, 164, 844, 434, 786, 992, 679, 463, 857, 851, 16, 83, 182, 106, 869, 846, 105, 300, 34, 542, 330, 101, 593, 881, 693, 195, 440, 52, 772, 959, 451, 810, 883, 914, 640, 424, 52, 690, 251, 831, 365, 101, 475, 919, 735, 82, 517, 391, 663, 482, 476, 62, 420, 176, 511, 197, 888, 739, 916, 694, 476, 531, 258, 123, 411, 417, 177, 244, 393, 346, 283, 554, 208, 77, 30, 848, 416, 670, 439, 7, 167, 579, 361, 184, 611, 429, 647, 557, 517, 724, 950, 261, 449, 853, 271, 184, 939, 170, 89, 224, 67, 179, 262, 240, 58, 581, 455, 827, 461, 940, 802, 27, 727, 873, 372, 962, 560, 804, 62, 806, 924, 673, 951, 197, 198, 946, 883, 60, 561, 533, 244, 278, 373, 28, 828, 220, 583, 379, 844, 129, 669, 877, 17, 668, 622, 744, 507, 634, 149, 219, 326, 668, 244, 732, 44, 264, 627, 423, 522, 372, 846, 721, 112, 681, 791, 209, 984, 435, 496, 738, 126, 110, 97, 611, 565, 395, 774, 334, 976, 402, 72, 807, 952, 272, 848, 728, 838, 444, 195, 573, 325, 570, 960, 53, 885, 571, 531, 751, 576, 438, 384, 560, 417, 271, 255, 776, 77, 545, 21, 493, 855, 442, 142, 412, 549, 759, 523, 909, 14, 925, 513, 413, 739, 326, 163, 740, 131, 807, 348, 962, 283, 853, 595, 995, 345, 269, 894, 697, 645, 701, 155, 904, 39, 929, 766, 172, 30, 199, 671, 1, 533, 261, 310, 732, 64, 597, 380, 256, 615, 999, 801, 391, 118, 703, 956, 646, 37, 931, 413, 540, 129, 262, 208, 513, 621, 871, 52, 443, 673, 546, 745, 66, 94, 529, 379, 789, 9, 112, 684, 10, 636, 538, 32, 232, 782, 953, 758, 2, 513, 601, 542, 198, 91, 27, 107, 307, 494, 80, 546, 928, 911, 957, 55, 773, 125, 310, 55, 883, 658, 159, 241, 245, 563, 695, 286, 47, 518, 773, 120, 480, 673, 612, 550, 464, 503, 825, 555, 697, 58, 831, 781, 494, 498, 669, 965, 836, 248, 830, 839, 629, 609, 764, 450, 390, 576, 272, 503, 91, 169, 154, 859, 422, 146, 146, 488, 605, 252, 625, 199, 232, 846, 841, 878, 955, 542, 981, 808, 189, 665, 985, 19, 452, 574, 646, 843, 14, 336, 560, 274, 933, 337, 296, 986, 856, 603, 693, 508, 486, 809, 443, 160, 654, 335, 922, 197, 221, 997, 862, 421, 97, 592, 853, 649, 737, 111, 508, 352, 248, 928, 731, 616, 859, 176, 932, 18, 717, 111, 513, 913, 30, 479, 358, 414, 768, 644, 288, 464, 917, 630, 652, 254, 991, 161, 504, 411, 522, 612, 755, 774, 512, 862, 243, 671, 909, 579, 850, 53, 632, 982, 956, 726, 711, 416, 618, 387, 547, 39, 198, 911, 8, 589, 327, 521, 678, 558, 48, 3, 236, 661, 400, 517, 977, 622, 924, 762, 3, 395, 714, 705, 844, 649, 625, 496, 993, 16, 35, 945, 619, 583, 428, 236, 631, 714, 852, 425, 880, 19, 380, 655, 580, 994, 846, 404, 195, 213, 672, 10, 984, 310, 774, 426, 133, 421, 14, 56, 743, 125, 681, 827, 514, 136, 278, 481, 171, 695, 434, 497, 188, 760, 696, 987, 820, 761, 56, 743, 9, 601, 794, 269, 802, 656, 557, 289, 496, 535, 427, 908, 427, 463, 203, 949, 854, 802, 640, 156, 936, 32, 676, 761, 75, 826, 392, 111, 955, 521, 123, 789, 161, 4, 526, 392, 230, 103, 791, 603, 139, 204, 353, 499, 990, 138, 495, 919, 666, 585, 787, 659, 278, 125, 552, 318, 451, 998, 116, 68, 543, 376, 208, 340, 107, 397, 232, 667, 795, 259, 807, 564, 486, 852, 152, 45, 679, 471, 594, 256, 41, 150, 89, 648, 996, 620, 139, 720, 979, 443, 262, 346, 984, 726, 46, 151, 673, 978, 763, 110, 985, 109, 746, 147, 431, 963, 76, 560, 565, 477, 287, 81, 22, 642, 569, 129, 321, 546, 957, 453, 527, 378, 152, 363, 495, 883, 194, 677, 403, 683, 916, 751, 852, 236, 7, 715, 616, 92, 13, 111, 974, 560, 771, 51, 424, 706, 216, 82, 713, 314, 231, 88, 472, 139, 558, 941, 59, 679, 670, 796, 771, 158, 499, 702, 767, 392, 209, 602, 726, 953, 841, 139, 459, 111, 192, 474, 456, 271, 106, 783, 841, 795, 821, 12, 256, 807, 746, 721, 766, 160, 284, 124, 823, 586, 822, 901, 430, 101, 696, 656, 391, 967, 355, 615, 869, 83, 685, 564, 877, 492, 237, 423, 684, 535, 184, 581, 739, 387, 883, 734, 225, 323, 645, 864, 29, 890, 168, 405, 463, 89, 685, 918, 138, 299, 207, 338, 564, 836, 811, 960, 380, 277, 41, 977, 169, 618, 421, 742, 598, 293, 630, 284, 243, 950, 294, 466, 147, 1000, 499, 633, 611, 394, 120, 235, 536, 288, 661, 725, 862, 773, 117, 996, 565, 866, 863, 537, 213, 734, 531, 813, 387, 526, 293, 704, 501, 910, 624, 556, 752, 274, 888, 877, 674, 139, 924, 401, 172, 15, 468, 933, 30, 124, 500, 31, 765, 812, 267, 778, 636, 723, 857, 487, 177, 231, 689, 136, 784, 634, 478, 895, 986, 622, 310, 693, 869, 467, 636, 773, 366, 388, 488, 642, 808, 551, 497, 30, 125, 834, 895, 951, 695, 769, 921, 242, 709, 393, 678, 886, 913, 399, 172, 52, 466, 701, 530, 274, 59, 418, 20, 766, 286, 507, 764, 416, 697, 752, 961, 7, 545, 376, 528, 401, 550, 106, 330, 651, 532, 74, 500, 447, 531, 637, 795, 806, 304, 323, 937, 259, 250, 956, 177, 964, 192, 96, 267, 961, 913, 957, 865, 376, 136, 722, 990, 333, 516, 935, 527, 318, 318, 578, 499, 137, 203, 314, 673, 973, 505, 230, 941, 654, 380, 806, 340, 416, 333, 84, 79, 990, 145, 311, 402, 409, 908, 164, 229, 507, 589, 226, 887, 453, 184, 118, 61, 849, 226]
    target = 10
    expected = 0
    assert Solution().solve(nums, target) == expected
