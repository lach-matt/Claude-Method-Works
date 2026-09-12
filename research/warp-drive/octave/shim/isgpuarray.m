function tf = isgpuarray(~)
% Octave shim: this build has no Parallel Computing Toolbox, so nothing is ever
% a gpuArray.  Warp Factory's CPU path is selected with tryGPU = 0.
  tf = false;
end
