import torch
import torchvision

class EncoderFactory:
    """Creates and returns a backbone that serves as feature extractor"""

    @classmethod
    def get(cls, backbone:str, pretrained:bool=True):
        backbones_dict = {
            "efficientnet-b1": cls.get_efficientnet_b1(pretrained=pretrained)
        }
        return backbones_dict[backbone](pretrained)
    
    @staticmethod
    def get_efficientnet_b1(pretrained=True) -> torch.nn.Module:
        backbone = torch.hub.load(
            'rwightman/gen-efficientnet-pytorch',
            'efficientnet_b1',
            pretrained=pretrained,
        )
        return torch.nn.Sequential(*list(backbone.as_sequential())[:-4]) 
    

