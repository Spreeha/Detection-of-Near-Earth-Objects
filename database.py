class NEODatabase:
    
    def __init__(self, neos, approaches):
        
        self._neos = neos
        self._approaches = approaches

        self._pdes_map_index = {neo.designation: index for index, neo in enumerate(self._neos)}

        for approach in self._approaches:
            if approach.designation in self._pdes_map_index.keys():
                approach.neo = self._neos[self._pdes_map_index[approach.designation]] #The NEO object at self._pdes_to_index[approach.designation] index will get updated as the .neo attribute for that approach obj
                self._neos[self._pdes_map_index[approach.designation]].approaches.append(approach)
                
        self.des_map_neo = {neo.designation: neo for neo in self._neos}
        self.name_map_neo = {neo.name: neo for neo in self._neos}

    def get_neo_by_designation(self, designation):
        return self.des_map_neo.get(designation, None)

    def get_neo_by_name(self, name):
        return self.name_map_neo.get(name, None)

    def query(self, filters=()):

        if filters:
            
            for approach in self._approaches:
                
                filter_results = []
                
                
                for filter_func in filters:
                    passes_filter = filter_func(approach)
                    filter_results.append(passes_filter)
                
                # Check if all the filter conditions are True for the current approach
                all_filters_pass = all(filter_results)
                
                # If all filters pass for the current approach, yield the approach
                if all_filters_pass:
                    yield approach

        else:
            for approach in self._approaches:
                yield approach
