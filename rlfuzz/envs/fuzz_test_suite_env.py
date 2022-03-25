import rlfuzz
from rlfuzz.envs.fuzz_base_env import FuzzBaseEnv


class FuzzlibpngEnv(FuzzBaseEnv):
    def __init__(self):
        self._target_path = rlfuzz.libpng_target_path()
        self._args = ['']
        self._seed = b''  # 指定初始变异的文件
        self._suffix = 'afl_out.png'
        self._input_maxsize = 32 * 1024  # 最大输入文件的大小
        self.peachflag = False
        if self.peachflag:
            self._Seed_Path = '/home/real/rlfuzz-socket/rlfuzz/mods/fuzzer-test-suite-mod/libpng-1.2.56/seeds/pngtest.png'
            self._dataModelName = 'PNG'
            self._PitPath = 'file:test/pit/png_datamodel.xml'
        super(FuzzlibpngEnv, self).__init__(PeachFlag=self.peachflag)

    def set_seed(self, seed):
        assert len(seed) > 0
        assert isinstance(seed, bytes)
        self._seed = seed
        self._input_maxsize = len(seed)
        self.reset()
