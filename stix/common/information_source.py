# Copyright (c) 2013, The MITRE Corporation. All rights reserved.
# See LICENSE.txt for complete terms.

import stix

from stix.extensions.identity import CIQIdentity3_0Instance
from stix.common.identity import Identity
from cybox.common import Time

import cybox.bindings.cybox_common as cybox_common_binding
import stix.bindings.indicator as stix_indicator_binding
import stix.bindings.stix_common as stix_common_binding
import stix.bindings.extensions.identity.ciq_identity_3_0 as ciq_identity_binding



class InformationSource(stix.Entity):
    def __init__(self, identity=None, time=None):
        self.identity = identity
        #self.contributors = []
        self.time = time
        #self.tools = []
        #self.references = []
    
    @property
    def identity(self):
        return self._identity
    
    @identity.setter
    def identity(self, value):
        if value and not isinstance(value, Identity):
            raise ValueError('value must be instance of Identity')
    
        self._identity = value
    
    @property
    def time(self):
        return self._time
    
    @time.setter
    def time(self, value):
        if value and not isinstance(value, Time):
            raise ValueError('value must be instance of Time')
        
        self._time = value
        
    
    def to_obj(self, return_obj=None):
        if return_obj == None:
            return_obj = stix_common_binding.InformationSourceType()
        
        identity_obj = self.identity.to_obj() if self.identity else None
        time_obj = self.time.to_obj() if self.time else None
        
        #=======================================================================
        # contributors_obj = stix_common_binding.ContributorsType() if self.contributors else None
        # for contributor in self.contributors:
        #    contributor_obj = contributor.to_obj()
        #    contributors_obj.add_Contributor(contributor_obj)
        # 
        # 
        # tools_obj = cybox_common_binding.ToolsInformationType() if self.tools else None
        # for tool in self.tools:
        #    tool_obj = tool.to_obj()
        #    tools_obj.add_Tool(tool_obj)
        #    
        # references_obj = stix_common_binding.ReferencesType() if self.references else None
        # for reference in self.references:
        #    reference_obj = reference.to_obj()
        #    references_obj.add_Reference(reference_obj)
        #=======================================================================
        
        
        return_obj.set_Identity(identity_obj)
        return_obj.set_Time(time_obj)
        #return_obj.set_Contributors(contributors_obj)
        #return_obj.set_Tools(tools_obj)
        #return_obj.set_References(references_obj)
    
        return return_obj
        
    @classmethod
    def from_obj(cls, obj, return_obj=None):
        if not obj:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        if obj.get_Identity():
            identity_obj = obj.get_Identity()
            if isinstance(identity_obj, ciq_identity_binding.CIQIdentity3_0InstanceType):
                return_obj.identity = CIQIdentity3_0Instance.from_obj(identity_obj)
            elif type(identity_obj) == stix_common_binding.IdentityType:
                return_obj.identity = Identity.from_obj(identity_obj)
        
        if obj.get_Time():
            return_obj.time = Time.from_obj(obj.get_Time())
            
        return return_obj
        
        
    @classmethod
    def from_dict(cls, dict_repr, return_obj=None):
        if not dict_repr:
            return None
        
        if not return_obj:
            return_obj = cls()
        
        identity_dict = dict_repr.get('identity', None)
        time_dict = dict_repr.get('time', None)
        
        if identity_dict:
            xsi_type = identity_dict.get('xsi:type')
            if xsi_type:
                type_name = xsi_type.split(":")[1]
                if  type_name == CIQIdentity3_0Instance._XML_TYPE:
                    return_obj.identity = CIQIdentity3_0Instance.from_dict(identity_dict)
                else:
                    raise TypeError('No known class for xsi:type: %s' % (xsi_type))
            else:
                return_obj.identity = Identity.from_dict(identity_dict)
                
        if time_dict:
            return_obj.time = Time.from_dict(time_dict)
        
        return return_obj
    
    
    def to_dict(self, return_dict=None):
        if not return_dict:
            return_dict = {}
        
        if self.identity:
            return_dict['identity'] = self.identity.to_dict()
            
        if self.time:
            return_dict['time']  = self.time.to_dict()
        
        return return_dict
    
    
    