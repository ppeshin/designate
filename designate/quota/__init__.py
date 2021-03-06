# Copyright 2013 Hewlett-Packard Development Company, L.P.
#
# Author: Kiall Mac Innes <kiall@hp.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from oslo.config import cfg
from designate.openstack.common import log as logging
from designate.quota.base import Quota

LOG = logging.getLogger(__name__)

cfg.CONF.register_opts([
    cfg.StrOpt('quota-driver', default='storage', help='Quota driver to use'),
    cfg.IntOpt('quota-domains', default=10, help='Number of domains allowed '
                                                 'per tenant'),
    cfg.IntOpt('quota-domain-records', default=500, help='Number of records '
                                                         'allowed per domain'),
])


def get_quota():
    return Quota.get_plugin(cfg.CONF.quota_driver, invoke_on_load=True)
