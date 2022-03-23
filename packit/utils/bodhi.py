# Copyright Contributors to the Packit project.
# SPDX-License-Identifier: MIT

import logging

from bodhi.client.bindings import BodhiClient

logger = logging.getLogger(__name__)


def get_bodhi_client(fas_username: str = None, fas_password: str = None) -> BodhiClient:
    """
    Initialise the Bodhi client.

    Bodhi will prompt for username and password
    if the values are not set and the session is not cached.
    (The session is stored as `~/.fedora/openidbaseclient-sessions.cache`.)

    Note for tests:
    * Don't mock the Bodhi instantiation via
      `flexmock(bodhi.client.bindings.BodhiClient).new_instances(bodhi_instance_mock)`
      what can affect other tests.
    * Mock this function instead -- for example:
      `flexmock(aliases).should_receive("get_bodhi_client").and_return(bodhi_instance_mock)`
    """
    logger.debug(
        f'Initialisation of the Bodhi client: FAS user {fas_username or "not configured"}; '
        f'password {"provided" if fas_password else "not configured"}'
    )
    return BodhiClient(username=fas_username, password=fas_password)