from jdaviz.core.helpers import ConfigHelper
from jdaviz.configs.default.plugins.line_lists.line_list_mixin import LineListMixin
from jdaviz.configs.specviz import SpecViz

class CubeViz(ConfigHelper, LineListMixin):
    """CubeViz Helper class"""
    _default_configuration = 'cubeviz'

    @property
    def fitted3d(self):
        """
        Returns the 3D fitted model parameters.

        Returns
        -------
        parameters : list
            list of Quantity 2D arrays, or None.
        """
        if hasattr(self.app, '_fitted_3d_model'):
            return self.app._fitted_3d_model
        else:
            return None

    @property
    def specviz(self):
        """
        A specviz helper for the app this helper wraps
        """
        if not hasattr(self, '_specviz'):
            self._specviz = SpecViz(app=self.app)
        return self._specviz
