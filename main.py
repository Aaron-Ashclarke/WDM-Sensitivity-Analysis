import numpy as np
import itertools


weights = {
    "Safety": 0.25, 
    "Traffic Impact": 0.15,
    "Accessibility": 0.15,
    "Cost": 0.10, 
    "Sales": 0.10,
    "Connection": 0.10, 
    "Jobs": 0.10,
    "Route Continuity": 0.05
            }

class bikelane: 
      current_score = 0
      highest_score = 0 
      lowest_score = 10
      average_score = 0
      scores = np.array([])
      
      def __init__(self, name, raws_scores):
        self.name = name
        self.raws_scores = raws_scores

      def calculate_score(self, weights): 
        self.current_score = 0
        for category, weight in weights.items():
            raw_score = self.raws_scores.get(category)
            adjusted_score = raw_score * weight
            self.current_score += adjusted_score

        self.scores = np.append(self.scores, [self.current_score])
        self.average_score = self.scores.mean()
        self.highest_score = self.scores.max()
        self.lowest_score = self.scores.min()
        

kent_raw_scores = {
    "Safety" : 7,
    "Traffic Impact": 8, 
    "Accessibility": 4,
    "Cost" : 10, 
    "Sales": 1, 
    "Connection" :5,
    "Jobs" :1,
    "Route Continuity": 9
}

greenway_raw_scores = {
    "Safety" : 7.5,
    "Traffic Impact": 3, 
    "Accessibility": 7,
    "Cost" : 9, 
    "Sales": 4, 
    "Connection" :3,
    "Jobs" :4,
    "Route Continuity": 9
}

west_14_option_1_raw_scores = {
    "Safety" : 10,
    "Traffic Impact": 6, 
    "Accessibility": 9,
    "Cost" : 8, 
    "Sales": 5, 
    "Connection" : 6,
    "Jobs" :5,
    "Route Continuity": 6
}

west_14_option_2_raw_scores = {
    "Safety" : 6.5,
    "Traffic Impact": 6, 
    "Accessibility": 9,
    "Cost" : 10, 
    "Sales": 5, 
    "Connection" :6,
    "Jobs" :5,
    "Route Continuity": 6
}

west_41st_raw_scores = {
    "Safety" : 7,
    "Traffic Impact": 7, 
    "Accessibility": 7,
    "Cost" : 0, 
    "Sales": 3, 
    "Connection" :9,
    "Jobs" :2,
    "Route Continuity": 4
}

kent = bikelane("West Kent", kent_raw_scores)
greenway = bikelane("Greenway Project", greenway_raw_scores)
west_14_option_1 = bikelane("West 14 option 1", west_14_option_1_raw_scores)
west_14_option_2 = bikelane("West 14 option 2", west_14_option_2_raw_scores)
west_41st = bikelane("West 41st", west_41st_raw_scores)


bikelanes = [kent, greenway, west_14_option_1, west_14_option_2, west_41st]

def combinamute_weights():
    weight_perms = list(itertools.permutations(weights.keys(),8))
    for permuation in weight_perms:
        new_weights = {
            permuation[0]: weights.get(permuation[0])+0.05,
            permuation[1]: weights.get(permuation[1])-0.05,
            permuation[2]: weights.get(permuation[2]),
            permuation[3]: weights.get(permuation[3]),
            permuation[4]: weights.get(permuation[4]),
            permuation[5]: weights.get(permuation[5]), 
            permuation[6]: weights.get(permuation[6]),
            permuation[7]: weights.get(permuation[7])
        }
        get_scores(new_weights)

    print("Name".ljust(18) + "Min   Avg   Max")
    for lane in bikelanes: 
        print("{:<17} {:.2f}, {:.2f}, {:.2f} ".format(lane.name, lane.lowest_score, lane.average_score, lane.highest_score))
    
    
def get_scores(weights):
    for lane in bikelanes:
        lane.calculate_score(weights=weights)
        


combinamute_weights()