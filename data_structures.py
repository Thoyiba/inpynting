class Image2BInpainted:

    #TODO maybe discard patch_size and gap
    def __init__(self, rgb, mask):
        self.rgb = rgb
        #self.mask = mask
        self.mask = mask // 255
        self.height = self.rgb.shape[0]
        self.width = self.rgb.shape[1]


class Patch:


    def __init__(self, patch_id, overlap_source_region, overlap_target_region, x_coord, y_coord, priority=None, labels=None, differences=None):

        # properties of all patches
        self.patch_id = patch_id
        self.overlap_source_region = overlap_source_region
        self.overlap_target_region = overlap_target_region
        self.x_coord = x_coord
        self.y_coord = y_coord

        # properties of patches having an intersection with the target region (i.e. patches to be inpainted)
        if priority is None:
            self.priority = 0
        else:
            self.priority = priority

        if labels is None:
            self.labels = []
        else:
            self.labels = labels

        if differences is None:
            self.differences = {}
        else:
            self.differences = differences
