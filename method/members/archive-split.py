#!/usr/bin/env python3
"""archive-split.py — the archive split of the compendia bundle (chat 129; chat-127 item 5, HANDOFF-81 Segment A).

  python3 archive-split.py                                  gate mode / dry run: deterministic, writes nothing (the banked golden)
  python3 archive-split.py --split OLD --archive OUT_A --live OUT_L [--main MAIN]   execute the split, guarded
  python3 archive-split.py --verify-archive PATH            verify an archive bundle against the embedded manifest (on demand)

The partition RULE (three full-match patterns) selects the archive: the legacy HANDOFF-*.md members, the r2-ch12*…r2-ch15*
instruments and goldens, and the READ-ch1[2-5]* / CENSUS-CLOSURES-ch1[2-5]* files. The archive manifest below was MEASURED on
BUILD158 (md5 3fc4111aea078f7b78fdc5b5cd1f4b0e, 598 members) and is the instrument's fixed data: 393 members, 3,694,933 B.

--split does, in order, and refuses on any failure: (1) asserts neither output exists; (2) parses OLD and requires the rule's
partition to equal the embedded manifest name for name, byte for byte, md5 for md5; (3) archive = the archived blocks in OLD's
order + an `ARCHIVE-MANIFEST.tsv` member; (4) live = the remaining blocks in OLD's order with the MANIFEST.tsv body rebuilt
over the main bundle's members and the live members (close.py's manifest_text format); (5) reverse guard: strip
ARCHIVE-MANIFEST.tsv, restore OLD's MANIFEST.tsv body, re-interleave every block at its original index, and require the
result's md5 to equal OLD's — nothing is written unless it does; (6) writes both.

Gate mode names no bundle: it resolves the highest-numbered `The_Method_1_6_BUILD<N>_compendia*` in /home/claude, reports how
many archived names it still carries (0 after the split), and checks that the rule applied to (live names ∪ archived names)
returns exactly the archived names — so the golden is reproducible on every later live bundle."""
import sys, os, re, hashlib
H = os.path.dirname(os.path.abspath(__file__)); HOME = os.path.dirname(H)
MEMBER = re.compile(rb'^<<<FILE: (.+?)>>>\n(.*?)<<<END FILE: \1>>>\n', re.S | re.M)
md5 = lambda b: hashlib.md5(b).hexdigest()
RULES = [r'HANDOFF-\d+(-[A-Z])?\.md', r'r2-ch1[2-5][a-z]*\.(py|out)', r'(READ|CENSUS-CLOSURES)-ch1[2-5][a-z]*\.(md|tsv)']
def is_arch(n): return any(re.fullmatch(p, n) for p in RULES)
ARCHIVE_MANIFEST = """HANDOFF-10.md	4306	6664d0bced3c5a5d546f3a85a115e809	23
HANDOFF-11.md	6111	783af426c5e8d5ed0490508a5bf40aa5	26
HANDOFF-14.md	7148	d66a8bb137e9596352b43f2e52480301	13
HANDOFF-15.md	7760	fecbd5a31cb8e793cf0af6c5020bd74f	116
HANDOFF-16.md	12490	bc078703d2b111c3dc6b2898940761ce	173
HANDOFF-17.md	15386	509c3635ac10e67a935a43fd84a051c1	208
HANDOFF-18.md	12941	e8961c2baa0ecfa9015e94803612bcbe	170
HANDOFF-19.md	18259	2eb4366a78299a459b910a11fd5b8836	234
HANDOFF-2.md	4363	596f012de36d1651854f0dda64cbe9ff	43
HANDOFF-20.md	18772	99e7eb73aa441919026a96910ddc4d37	242
HANDOFF-21.md	19939	25c776aaafd9cec0746156346190cba6	258
HANDOFF-22.md	17582	a3b12b52f91eb93b0ed79e62ca187946	228
HANDOFF-23.md	11674	8ea6f77bfcd6caebeadac0116314604a	151
HANDOFF-24.md	12339	be9561ad057802c986de9f95560de7d6	161
HANDOFF-25.md	12936	a965616eb1adf0db6ee654b5c6a7ce73	166
HANDOFF-26.md	13919	676c068b5e11778af472a6edddc6f783	174
HANDOFF-27.md	15302	529848519511ea9b530e24ca375c52d5	199
HANDOFF-28.md	21629	6047b41cd90be64a9b08375a3b2ee599	264
HANDOFF-29.md	27414	fffb7f835fe1918ddbca309323d49ac6	331
HANDOFF-30.md	25342	ecfa083fba58ff696cfb4a0f18f71710	311
HANDOFF-32.md	24305	513505e4a50f8d626339bd47a040a542	303
HANDOFF-34.md	15184	707bbba465bae363fccb1d4a6f3393bd	187
HANDOFF-35.md	16952	17ab54493af5ddbb23f12a57578f8da2	208
HANDOFF-36.md	18851	e4d2d43d008a9ada1224f59f23d5ae43	234
HANDOFF-37.md	16281	818372721a4c0e5e581bb1902a196fcd	202
HANDOFF-38.md	16985	38a60795dbc59a736b1e894a751589c8	209
HANDOFF-39.md	18691	b566a69f7d0364037f0645b8532b3324	230
HANDOFF-4.md	4914	e4f347be86010da7eaf4d73193dfed24	42
HANDOFF-40.md	19171	dc93e4d20f832b9312c18cc0ca5f5a90	232
HANDOFF-41.md	20920	5382cd0b036315074c552281d5ab5ba7	245
HANDOFF-42.md	22589	c0b037d83c78618e2871e7dace1dc3de	266
HANDOFF-43.md	19705	31a6d75fc99a3d9c530f29a8cd1ee390	229
HANDOFF-44.md	17795	35034fec1b60701603fd705c695ba7fa	211
HANDOFF-45.md	19807	a006423bf4cb187cb6608d7322ed89b5	227
HANDOFF-46.md	21143	fd931ffdd56e61555881be55096e8cb9	238
HANDOFF-47.md	23589	2e8ce89f6bf9bb8adbdfc5f7c04aa5c6	264
HANDOFF-48.md	31480	6ccdfac9893483316bef56be947e0956	351
HANDOFF-49.md	25114	10a73477a108cd83bfd53a4b2091bbdf	284
HANDOFF-5.md	4005	0e0dfe368d4e75ebd4050aeba90fe7d3	38
HANDOFF-50.md	26991	2fc8a106946f63efb9f75cb5ed1d52f8	304
HANDOFF-51.md	22315	ae6f180ba2b7aa8bee496ef09b3e79ce	268
HANDOFF-52.md	27049	c0d2a723320b497d87e8625aafb7f175	317
HANDOFF-53.md	7581	1caab8363689ef356467b6ae9f7801d9	97
HANDOFF-6.md	4590	2464a873aacfca6c68d076ae5d4b5c68	37
HANDOFF-7.md	4667	133e0a1190b6fc92682e42e46d6a1092	31
HANDOFF-8.md	4698	32519b5d7dea1ab2cfde2e3d3f955316	27
HANDOFF-9.md	3922	73f3b847044a600304b4a4364b9a66e4	24
HANDOFF-19-A.md	10807	d67079b8d076be32f327d6870ff263d9	32
READ-ch12a.md	3490	12c9b59e2520674eaa4a34f5e47742e4	23
CENSUS-CLOSURES-ch12a.tsv	301	ab5dbdef64b1b11a53935631d9e4392a	2
r2-ch12a.py	724	00ef72b864a9891e664ae47b77a5de72	13
READ-ch12b.md	4699	6f29d13c08ae3b864cb7cc10a5b9aef4	27
CENSUS-CLOSURES-ch12b.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch12b.py	3837	08eb3d5b76f70c2b8f5074f1743349ef	52
READ-ch12c.md	16244	78f9d04f0427c64bdcff46839eaaeaa4	47
CENSUS-CLOSURES-ch12c.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch12c.py	11465	acf13fbd12fe94d52c8e50fad508805a	137
READ-ch12d.md	6175	51c0c74b26bc62d574f16e68e23988d2	26
CENSUS-CLOSURES-ch12d.tsv	352	a7dc4d322833135fcb10dc2c3747278d	3
r2-ch12d.py	3285	62b9383c073a1868eb26e397a20d112f	38
READ-ch12e.md	8926	9b1b0521b1e40a14357f36f87405c56f	34
CENSUS-CLOSURES-ch12e.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch12e.py	5164	ed83a691d1b4bb1d7bed6c4da85b5733	60
READ-ch12f.md	9997	23b930badf9804b45ccc8ece79ede025	30
CENSUS-CLOSURES-ch12f.tsv	220	f13fd002d1c14cebf6d06d097f385aa9	2
r2-ch12f.py	7957	729bc2aa423e9d0ddf89f49d210535bb	145
READ-ch12g.md	6836	6a3d91d95b8070a7f670f2c542820ce7	28
CENSUS-CLOSURES-ch12g.tsv	233	5d6413d526f901f61027c97eeec0d9a7	2
r2-ch12g.py	5159	e5017aa55ee57e5657f2350e2e4bd930	78
READ-ch12h.md	5900	176f10e105b34526fc70f16ffc6afd8a	28
CENSUS-CLOSURES-ch12h.tsv	220	ea9afda6fef6e3ee696022fd94ac6941	2
r2-ch12h.py	3347	2fdeb479d9693e814cc48539936b7dd7	53
READ-ch12i.md	8772	bf39d2b12f7ff66f0ea66b1bf2ccee09	33
CENSUS-CLOSURES-ch12i.tsv	617	71b9890b94c14c481d2c62811faa606d	3
r2-ch12i.py	7229	256b90d4fcc8dc500a5ac47e016b9b99	114
READ-ch12j.md	6894	27c04f3551161eae52bdb58ac1be80a9	32
CENSUS-CLOSURES-ch12j.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch12j.py	5809	cd469dd1cedbc9e9e66dadc79e98f78b	84
READ-ch12k.md	7976	d20987369ad7878ae9db13614c66ae59	31
CENSUS-CLOSURES-ch12k.tsv	1874	fbc718f7789488cebe5e0310387fba34	8
r2-ch12k.py	6337	6aee59256315d0f03949f86da3c1c526	77
r2-ch12a.out	120	9a7cf824324b1732a1d93aa4e87fe0f9	1
r2-ch12b.out	2846	a59ff8f656f0bb428c7e045d6f5e4863	33
r2-ch12d.out	1232	55e3f02eec3b719fad35de35eb1da1aa	8
r2-ch12e.out	1928	87aac2b1d1a463651678f3e04fda3dd2	12
r2-ch12f.out	4328	655be2bf4592760d9022b28b1c8b3122	22
r2-ch12g.out	2214	4121c725e1b7ff9d86ffccb3dfdd4fda	15
r2-ch12h.out	1970	85c50b4912adae4bcef0a0f28722678a	27
r2-ch12i.out	2341	0fe58eeeabd4caad3aa0e891e29e8709	17
r2-ch12j.out	2272	fc2c7aea3b1597ef87e0298c62719572	14
r2-ch12k.out	2720	4901eff29e36fbaf9ce05d09a251fb48	23
READ-ch12l.md	11525	da79d49fdbc13ff5c24921e472608a12	38
CENSUS-CLOSURES-ch12l.tsv	746	c3bcd2d7241004e3a592dae665264a7a	3
r2-ch12l.py	10896	dc7d6dad8dc5dff676e9e74b12e84e47	117
r2-ch12l.out	4665	1abd90a88248f2c90e73c7b108e93b0d	37
READ-ch12m.md	7871	9e5bbaca41df19373034ac08fa83031c	31
CENSUS-CLOSURES-ch12m.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch12m.py	9245	97ddb4a88fb9509cc53cab24ad3d8fe8	121
r2-ch12m.out	3226	a05d15fb889a003301636337f4602267	20
READ-ch12n.md	6263	6f9c06af738f139fd402aa18fa02d1b7	31
CENSUS-CLOSURES-ch12n.tsv	431	179556093b47137151bd23a621e07819	2
r2-ch12n.py	7412	d3dfd05041ff60dce468db86ea2f9bfd	95
r2-ch12n.out	3837	be0433ba9adc2827831995f18d0d0951	29
READ-ch12o.md	5667	91a567c7c4255a048f151b86149450e7	28
CENSUS-CLOSURES-ch12o.tsv	398	79d452d778a363665e0e6499379b3782	2
r2-ch12o.py	3496	26f809956a9e6f092e6245631c6e7fab	36
r2-ch12o.out	2401	503e2f188b43f7ad29820532dd3e2065	17
READ-ch12p.md	3827	3a919c716080e2432162be6c3263840e	24
CENSUS-CLOSURES-ch12p.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch12p.py	3644	78eca3d702358b6c9dbdfc2175455022	34
r2-ch12p.out	1144	e1a98f5424016794d4f0abe2ceb5ad65	6
READ-ch12q.md	14145	2d60f3c3f232421364dc37486c0b0e73	44
CENSUS-CLOSURES-ch12q.tsv	638	1c31749e2722a753d1a73a6a25faacad	3
r2-ch12q.py	14588	d913db4891d35f2efee99815dbe098ea	140
r2-ch12q.out	6432	8d9972de516ba32c9023c299b0b6f8f0	37
READ-ch12r.md	8199	3408fd641cf58f63a6e21b2a1597fb10	28
CENSUS-CLOSURES-ch12r.tsv	917	a5de9005cce5ce23d1f5536d3f8ffaa0	4
r2-ch12r.py	13834	8b8c2cd3c7f864e037f23cfd0985415d	161
r2-ch12r.out	4605	806e84e71606c9e2c6067425ae83bce1	26
READ-ch12s.md	8095	b6a20d6280dd929c541db1aa120621ef	29
CENSUS-CLOSURES-ch12s.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch12s.py	9413	04e191f4a31d9f48399f1217e48a7433	110
r2-ch12s.out	2841	6adc5d228b2083ce17e2622351e2da51	13
READ-ch12t.md	8526	3b3bc9b12fc7ed01f09a7e9a755ffa44	28
CENSUS-CLOSURES-ch12t.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch12t.py	10986	39a03d79857efb9aaba799a9690be7d1	125
r2-ch12t.out	5566	f2e084b022496082730c13fc4f7e625c	34
READ-ch12u.md	5997	56f82f32a84eb6d8fb750cb5dc7bf15b	26
CENSUS-CLOSURES-ch12u.tsv	199	c1425a8fa0c464b6d325904eb380c5e4	2
r2-ch12u.py	4143	98ba4a6d9276ba91acdf2b1dce93ff25	36
r2-ch12u.out	6135	f47e5b0d65c2fb0be13a632adda27e80	29
READ-ch12v.md	5012	b08c7e9e3ff5b5d0fc759582b1b65f3c	25
CENSUS-CLOSURES-ch12v.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch12v.py	3470	cae2f0a59c7e0673f7080076767a5afb	30
r2-ch12v.out	958	8f72dd24c2adb757cec4141393f32e28	6
READ-ch12w.md	6721	caf17cafa6be27799485bdd8875d41fc	28
CENSUS-CLOSURES-ch12w.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch12w.py	7256	cba373e4c4312ec9480232529988d266	64
r2-ch12w.out	2468	81f7666bfae3afcea154f43d8a3091ae	15
READ-ch12x.md	3911	8f7c1c160c6c67d2573bfdff69a0dc5a	23
CENSUS-CLOSURES-ch12x.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch12x.py	2714	792dfde1385bd5d54dd368d6b4ac12b5	15
r2-ch12x.out	1751	75f1990a601e725e73106e40b1ed0eec	11
READ-ch12y.md	8297	1189a708f1d5d2048155e61d5a91f9fa	38
CENSUS-CLOSURES-ch12y.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch12y.py	11933	04a76748bb241255341adbf36c03106b	177
r2-ch12y.out	6573	42a33746ffd10a027b22991e016addc9	63
READ-ch12z.md	5867	89a1492fb842a5e5a04ba14b72f2a7b8	27
CENSUS-CLOSURES-ch12z.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch12z.py	7913	7e5161aafb0d18b151481a7dcdb254f7	111
r2-ch12z.out	2392	e006ba896e24f1ee4e011bc63d17479e	22
READ-ch13a.md	5234	1142622bb96aa3ea5d1504340f820b14	28
CENSUS-CLOSURES-ch13a.tsv	248	df2dc337ff3edb35ab121febcbc5ed6d	2
r2-ch13a.py	4721	6c8a35f5c4f9e735be9c883e593c6116	57
r2-ch13a.out	1801	2a9f0415a2e5a450243ff1f1f6fae74a	13
READ-ch13b.md	7892	5aa5f89b2455b969aa58b4f9a47d39ae	36
CENSUS-CLOSURES-ch13b.tsv	1237	83096d7a5db122dce3e8a956e85e4496	5
r2-ch13b.py	7301	f6cd8b2b15411c84911e1733470ee0b4	124
r2-ch13b.out	3712	4613302c69cebdd3d262034e11372ba8	50
READ-ch13c.md	10001	d9c6796869e2650c3cfc823a72edaece	36
CENSUS-CLOSURES-ch13c.tsv	502	62736b77736b2019239a5bb28cde335f	2
r2-ch13c.py	4771	6e1f5a729ad6637f48479f22c864a087	96
r2-ch13c.out	1957	794d12cdd0032773b80c5c9ffe4d50cf	35
READ-ch13d.md	6622	8458bb0667d75c185552061bf186dee4	28
CENSUS-CLOSURES-ch13d.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch13d.py	3240	dd9a6071a21ff06bb6088364b42b4722	59
r2-ch13d.out	3379	0a7dbe6b2d3d2babf31959230d3eb1f1	48
READ-ch13e.md	12328	cdf28e189ef6ff0001b74d8ea5ec9b73	50
CENSUS-CLOSURES-ch13e.tsv	717	e72bb65d6e737787309bcb33c58df1c1	2
r2-ch13e.py	13410	c51a65890ec25119806b7a7e8902c69c	252
r2-ch13e.out	6768	9a0bcdc065adb90149e4083a8036decb	85
READ-ch13f.md	10292	99f3c21423d483947342a70c54d8526e	54
CENSUS-CLOSURES-ch13f.tsv	677	2ffd35192dd3cc184e2978d669ada489	2
r2-ch13f.py	7109	11b81974b4211c875be1a6ff3f6e2310	123
r2-ch13f.out	2700	2dc8c9d8fc81c852997dcb0a54160c23	49
READ-ch13g.md	8414	9e5a0e10d2e873a93d9d272c30b83d0f	45
CENSUS-CLOSURES-ch13g.tsv	583	7bab54863d8dad39c3d8d8955516cc1e	2
r2-ch13g.py	5798	03eb998ea7007cde63b6064ce0a713dd	106
r2-ch13g.out	2634	aa32f589dcf3b8cf8f1aadcaa114abfb	56
READ-ch13h.md	9635	d3dd2b32746089f2d7dbe4f339c85b28	116
CENSUS-CLOSURES-ch13h.tsv	464	19ba723ddc7a731c3015588c10967769	2
r2-ch13h.py	11062	8bd6094f80ca4504044b7b7b6515fe45	220
r2-ch13h.out	3340	daafc3f17e5cd7a9a04d493d7748c8df	41
READ-ch13i.md	7120	eaea18cd1a65fbd50f6710ad0faa3b42	97
CENSUS-CLOSURES-ch13i.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch13i.py	3881	28cb5551d25aea1037a23cd43185e687	69
r2-ch13i.out	4738	76cf81364b4509ddd03ecca33ec80505	43
READ-ch13j.md	15806	19bf02d78d92a2cc4324fdbacc47f2a9	197
CENSUS-CLOSURES-ch13j.tsv	3662	e4dad56fd55b3de2a9fd8cb19b466762	20
r2-ch13j.py	22693	b7ed6a7e5b3babebd39b28b138635183	435
r2-ch13j.out	9907	2eff9e97699fda47de1d998ae5169dd3	87
r2-ch13k.py	9230	d30323a2ec257fd8b6a5eb292b694a42	155
r2-ch13k.out	14981	0b0feb5ae15bc7ae5d38c69b661f2265	153
READ-ch13l.md	13504	b009628c05405851efeec2b443067574	182
CENSUS-CLOSURES-ch13l.tsv	710	16846fecb6e6042056aa1ccd50c9459f	3
r2-ch13l.py	14658	d3f476886f829ce63fd28f5b7f7e19cd	247
r2-ch13l.out	5187	1b04f0e63c7dce4954d2083fa8661232	62
r2-ch13m.py	7892	49799b4de8f0e93190877a1c2b25f384	140
r2-ch13m.out	8873	d15b0e3f4f5d58cc9520df99abe69092	112
READ-ch13n.md	14515	9534c20e2b4831e139234364def471a5	193
CENSUS-CLOSURES-ch13n.tsv	986	820ffed3bf201408739b4b880ac06d80	6
r2-ch13n.py	11000	150fabf5277bc6f55899b6991401e14a	214
r2-ch13n.out	6362	57e6a3105a56084358a472783bc12749	84
r2-ch13o.py	7406	b00a27ef5664b3b65c0aac567834f649	135
r2-ch13o.out	7099	8f1e8d747cbdae34fda23f4ab194b011	85
READ-ch13p.md	27071	10b56a37580df973bf0c67f1444fad7c	351
CENSUS-CLOSURES-ch13p.tsv	3610	e49ed8420f1a93c80a4f1264feca6432	15
r2-ch13p.py	22590	08fd5f414e689ffb2a6279e091c6076b	433
r2-ch13p.out	9543	30e7afeae9b4bf875e3f9da7f4a92bed	148
r2-ch13q.py	12841	221bca6c3f9fab318a974c44ea6f1735	235
r2-ch13q.out	16442	1e1479f4461494cac988a6519f35717a	225
READ-ch13r.md	19113	1871a400970bf1326b94a6cf6354d7f2	261
CENSUS-CLOSURES-ch13r.tsv	1027	63d0fa9669bf5c1c8ed0210a8cec6208	3
r2-ch13r.py	18894	27ef05a4a4dda287d1d41b00b6944b52	361
r2-ch13r.out	6945	71fef61e43f5b887e4efc1668ca36caf	102
r2-ch13s.py	6905	ed000134538c788880fecde81024f5e0	148
r2-ch13s.out	16171	5ce0795e5ff8fa11e14b9e09df500624	198
READ-ch13t.md	15692	dd1369e31a15bff81d8fcc2503a73258	202
CENSUS-CLOSURES-ch13t.tsv	5054	df79123fe9cbd511d9402d6cb9cc3679	18
r2-ch13t.py	19212	ba52efe149e8924fef4ccbcdca9af8c2	381
r2-ch13t.out	7037	904428e4c989ab96f15753a6724626da	105
r2-ch13u.py	10195	854143fc7b766769589c6828bc593889	185
r2-ch13u.out	9771	f75dc9510c097cf2074e00c224627e72	119
READ-ch13v.md	14023	7717d5e81db173d0e973cab7cc6c839f	186
CENSUS-CLOSURES-ch13v.tsv	927	866253733737c5ccfef0479a783cdedb	3
r2-ch13v.py	14347	0adca44573c87f4c47bcc2bf7b0a18f5	250
r2-ch13v.out	9123	4b819bdd1ce51a759c480acf74f25227	139
r2-ch13w.py	12179	955c2cec00957689275e5b7037f6ad72	224
r2-ch13w.out	9089	7266ad6d565784509904c2a7aab42b8c	118
READ-ch13x.md	14566	083330a0510700971595c19ee31df7f5	193
CENSUS-CLOSURES-ch13x.tsv	1320	b13c84e117957ad974132a84fea19382	3
r2-ch13x.py	8678	9e9c4541bf2a63bd954b86050e4df775	193
r2-ch13x.out	2440	938fa1f6d4357b977dae6ead9ef10fb6	57
r2-ch13y.py	9804	a0faa418b312b8149b9fc7db519e25ea	217
r2-ch13y.out	7206	92ddfa236eb8bad79382853f90f6248b	109
READ-ch13z.md	7524	bbae559dc757495503ffcb83f88f2c6c	98
CENSUS-CLOSURES-ch13z.tsv	712	571b5b13231f2a3793033170a876c551	3
r2-ch13z.py	8115	b4419fe15181af2cab52ea098cd63cb1	158
r2-ch13z.out	4238	353f472ebdd70d9045f02633b8efdf9b	72
r2-ch14a.py	9881	b50b2ecb6e7fb09dd9af426671436fba	225
r2-ch14a.out	13544	acb3394856b8443ed46dfe00a560b1a4	158
READ-ch14b.md	14181	9f15c07f3a882a0b1d1162ae335ae896	219
CENSUS-CLOSURES-ch14b.tsv	508	4120571683e294b27ab29b9104248c0f	2
r2-ch14b.py	21857	bb38e9e960b0e7706b3a9f578701344d	449
r2-ch14b.out	13082	9325315cb55c5ac1ca565254483feb4e	175
r2-ch14c.py	11475	5b5398382de33a3a01165bfdf456f25d	245
r2-ch14c.out	10950	565b59cce62fe691225d29b5681b446a	132
READ-ch14d.md	11535	e4453de51048f4ee283e23b5f184e8ec	158
CENSUS-CLOSURES-ch14d.tsv	1312	9545304e70a85accdd4198a80530bd1c	4
r2-ch14d.py	10882	87b2ce1aec734d01258a6dbfd07f1e9e	202
r2-ch14d.out	5583	5b13967680d8e990f00630a9adf46b98	82
r2-ch14e.py	9269	1f8931abc8124adeced4ad18e8c25ca0	185
r2-ch14e.out	8144	1ee1da144fb5493feeb3ee85564b41ef	119
READ-ch14f.md	15942	225ffd0e96b10573a3e01cd9eaf2cf8b	243
CENSUS-CLOSURES-ch14f.tsv	1009	1a244cf40469667db488b4fbd52f6f88	4
r2-ch14f.py	12442	d3552daae8be66b510b14137591739d4	201
r2-ch14f.out	7784	35f7068c1b5abb265b19b906c79a80fc	125
r2-ch14g.py	16169	106ea7df5648cf9ac057f105309bdc0a	288
r2-ch14g.out	14016	436ae11b354a002ef946884398666306	192
READ-ch14h.md	17497	b8be0f6fcd5c8d1d7b4199d1d8274274	233
CENSUS-CLOSURES-ch14h.tsv	507	269c45b6fe7ae2e3f593978d4eee4f9a	2
r2-ch14h.py	21046	df9034dedbcb62dd442eaa2d767605ed	362
r2-ch14h.out	17870	b788fa4d7582fee131e78dbf32f704bb	263
r2-ch14i.py	14675	94f793a52fdebb23137e2cfdfaf2dbe8	296
r2-ch14i.out	14454	de696a7af5b467ed41d3cd770ca191d3	208
READ-ch14j.md	15599	325db6fe0e180dcd5272b5b854bbec5c	201
CENSUS-CLOSURES-ch14j.tsv	1274	d40cab2f06686a2dd02b97d21f505469	3
r2-ch14j.py	26941	c10c82fe9ef526356ae91effb5797578	399
r2-ch14j.out	20756	11cfd829c7d954594914db7e83146b68	288
r2-ch14k.py	17979	633e987df6e25b9a1de19198d24fdd97	285
r2-ch14k.out	19698	5574a7226a050254f8c0a6b1677d9db1	268
READ-ch14l.md	15401	25dd8c49d014498c9cc8cf61cbb716eb	198
CENSUS-CLOSURES-ch14l.tsv	769	e0c99e87a2440515974ffb15962854fa	2
r2-ch14l.py	24267	0f81df8ff0dae9e69612ed9cab2af09f	410
r2-ch14l.out	12977	c4803f26c520d8a7d25c85eabe4e1768	124
r2-ch14m.py	18696	c8aee0efcc0e147be9ae04932432614b	280
r2-ch14m.out	13398	fc3fee6a86c97cb977ad0e9846983490	97
READ-ch14n.md	13607	b69ec0a47043b188b742d852d5e046bd	198
CENSUS-CLOSURES-ch14n.tsv	433	f379df8ceef26a07c3ae8d26a8199a5f	2
r2-ch14n.py	11479	0cfab60276ab95ed85d4c0c6efcc6c1f	230
r2-ch14n.out	5540	0259aeae0c5757c3317c5aee1e94cf44	49
r2-ch14o.py	9627	1ddd04a8c97d05331fead3c4fb6b8baa	180
r2-ch14o.out	9247	9923bc2d835a9e785159d8bf7bf7b651	89
READ-ch14p.md	13405	33a02fc2c2d57e2e6401d84b439f2e17	200
CENSUS-CLOSURES-ch14p.tsv	537	5ac46d029942cb5b53abeaf3d6416803	2
r2-ch14p.py	20432	9c966e546f4c341d8c0966a8ada0f9ef	312
r2-ch14p.out	15920	fee8fd644e3c6c320ff16e8b901d7397	167
r2-ch14q.py	13033	c86a395295202673da0d09fd466ca0c8	183
r2-ch14q.out	12769	88b2d69d3f761064405974831b8d99b2	115
READ-ch14r.md	17246	94994ea3866e36a94f751b3be894ab0f	237
CENSUS-CLOSURES-ch14r.tsv	1412	fe304becffb89f42c2428aad708ea639	4
r2-ch14r.py	27109	8b20bf212c5bc095fe4e8fe5b49cf8f8	427
r2-ch14r.out	18200	1693fbf1788a9ba3e2074e4e329fb43c	232
r2-ch14s.py	10829	a9dddf9e2ae0fe2c05e02fd2314c488d	186
r2-ch14s.out	11750	692a7ecbf03adc92a5c9c40e5ec75ec2	126
READ-ch14t.md	14112	228e8fd8b5c2554ba4b27d264a19fe94	220
CENSUS-CLOSURES-ch14t.tsv	671	b8e98e8e85f3285c53dd724428910fa2	3
r2-ch14t.py	14657	59a1adaaf751f72e593b96ff4c582712	267
r2-ch14t.out	6683	36d7afbc416086e85e72c9f8456f14b3	117
r2-ch14u.py	12020	a404ec11f878bb603f3d5085fdd13984	226
r2-ch14u.out	12726	3eaa668dd328072af93f9fd43ac95327	179
READ-ch14v.md	11781	1e5febdc9ba0965754fbf14b405fcec7	153
CENSUS-CLOSURES-ch14v.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch14v.py	14899	656b524c1c9556c61a215aae7eca231a	289
r2-ch14v.out	5685	1c7abe1667fece10d7f449e0af4e3387	84
r2-ch14w.py	7846	c2852c47ab925c8cb52bd37395121894	146
r2-ch14w.out	5950	2e3145719b07ab48cc6f4c19be336a04	99
READ-ch14x.md	13559	95186e06bc8d7479389326b0f93f9999	166
CENSUS-CLOSURES-ch14x.tsv	898	40c959837d532080bd2d024a939d9abb	3
r2-ch14x.py	12031	4c65e30c78b8c9b286af3b93c27188a5	214
r2-ch14x.out	11760	6921d279fa0b55f4c637c68408e1a0fc	170
r2-ch14y.py	12907	dc3e9336d6c834b0ecfd5f7d6b375295	220
r2-ch14y.out	12494	e04bc1fb88f4bb05d5ca9bc76de6782e	171
READ-ch14z.md	17121	0119f4cc8bfe2d1b41453ff3c1f107de	224
CENSUS-CLOSURES-ch14z.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch14z.py	12952	d4d380e96badbcc896943eae5eb9b9ab	250
r2-ch14z.out	7712	c6edbfacb1b334a47ac0db4d3acfb01c	117
r2-ch15a.py	12197	6aada0a15e01b919ae0237a33c8be78c	254
r2-ch15a.out	18539	8c76814b0cc73e173e3a6deb0591f865	284
READ-ch15b.md	13205	bb753d40ad7da3d527197b1ee8174945	179
CENSUS-CLOSURES-ch15b.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch15b.py	13061	7fdf1f651d7f64c095ed6dede38c0013	227
r2-ch15b.out	9045	a438e85b8b80d7ceb12b77fd81e36441	125
r2-ch15c.py	10108	16e4d5dd2d71f35ae19bdafb729cf302	189
r2-ch15c.out	11439	bdfc010d81e5d1b2ef32780f9276195b	156
READ-ch15d.md	12046	c45960f07366c3f06a1e74aa5af04b03	157
CENSUS-CLOSURES-ch15d.tsv	1842	92d8726e01d66dcea0b66885242eea19	8
r2-ch15d.py	11974	caadf81d5642978c60ed7c723792308d	196
r2-ch15d.out	11551	556b83a620b28e0997218161f4527083	157
r2-ch15e.py	12245	b7b3500baa354fbfb832ce45800fd151	214
r2-ch15e.out	19655	a2c06d906f2be32857011aa1ccbe8320	275
READ-ch15f.md	12100	bbd648049e1572bb7da3ef49029854af	163
CENSUS-CLOSURES-ch15f.tsv	1082	1acf182d413d8d8acd9b0743bac4c227	6
r2-ch15f.py	15290	4137504f9ca1deff744ae330dc177518	291
r2-ch15f.out	18967	91d6b1499232d9036bf94a41d40759d6	233
r2-ch15g.py	10452	50ba32e4d8b19263b1f5e6a6d5d1826d	218
r2-ch15g.out	14051	6df208348d88ec4e9783b5cbc522d066	208
READ-ch15g.md	11685	3652a0fa5b039423ae6b3f56b2d70729	153
CENSUS-CLOSURES-ch15g.tsv	576	1062b33588a9127440fb1feee99cbee8	4
r2-ch15h.py	11136	24f202f76c74db3ca1702fbbda9922e1	211
r2-ch15h.out	6691	8bdd3aea516fd66d14e84e0376ccf9ce	82
r2-ch15i.py	10062	9cc0715875363aa681c73396ef1069ff	184
r2-ch15i.out	8074	833fa62a3188277470391fa27d3617d3	99
READ-ch15h.md	14244	500b54a965e9493b5c0dd11e87091f2e	193
CENSUS-CLOSURES-ch15h.tsv	1230	3a38f0a9e9bde74b07cd1b0b073eabc7	9
r2-ch15j.py	13213	045a5cbd1946bd306eb2d061a9778d27	248
r2-ch15j.out	10308	678764504684094d4e30e0ae29bf6975	168
r2-ch15k.py	13352	4c52f7687b419a1a9b133cbcc09ee661	250
r2-ch15k.out	14774	3a41d850ad71fdce44e314d88dab241b	177
READ-ch15i.md	10384	d92665a96e4a7605aff2b0a2c6470150	140
CENSUS-CLOSURES-ch15i.tsv	830	3ad59345613e3675c2eaa393ddcd8993	4
r2-ch15l.py	15865	35b80de2fb504a11fc0a98a5fec0b207	279
r2-ch15l.out	13012	a31698583f338b570c0278977d9e6314	172
r2-ch15m.py	16384	022e8479b09bde11e011d41b2cc9c5d1	273
r2-ch15m.out	20203	db20fad25dd89f8f07bccf09e3853dd9	240
READ-ch15j.md	13313	72b6deee2982c626bc3a936c17e9a82b	188
CENSUS-CLOSURES-ch15j.tsv	762	0d752e879a800ea93777ee36a6f18673	3
r2-ch15n.py	13703	3b7bcccee946826bb7b877ab3ecf75af	249
r2-ch15n.out	9529	20cdb902b75cb343e8e8f22846ca663c	134
r2-ch15o.py	15456	2fc11316695c429578845352bfee7b78	306
r2-ch15o.out	14485	65dfc401fbff50c76461f94aa1eb6e61	176
READ-ch15k.md	10045	28bf73dff05d031203a3cc1630347d8b	134
CENSUS-CLOSURES-ch15k.tsv	777	dd3a5bcc23c16dd26514966f5a36f7c4	6
r2-ch15p.py	14939	4d5468fe278cbf3ae1807472814a8f60	306
r2-ch15p.out	10193	bae8b29c4a9b3f7445ae778fd170c011	149
r2-ch15q.py	10089	e3c8d432130aa511ec110d8b2d75329b	205
r2-ch15q.out	10181	9cdbb225568db197afb9dca1a15ba8a3	126
READ-ch15l.md	10964	03c645623525ded643173021c36984bc	140
CENSUS-CLOSURES-ch15l.tsv	18	2deb87a95756d48874feff7dd5098af1	1
r2-ch15r.py	14030	f1d133d63e9ea3dcbca19ac835f3d256	275
r2-ch15r.out	15105	2337ce9ecb2dcf5036c099dbfc31ee72	206
r2-ch15s.py	10484	be5444369e1771be3d9ed67a1125ed93	219
r2-ch15s.out	18563	e7625d150ed762157977b05396130e49	211
READ-ch15m.md	14545	59f3dd783af554bfeca5ed157229bc9c	211
CENSUS-CLOSURES-ch15m.tsv	873	71a924bf0cca6cbb6b746a0b0718b9d3	2
r2-ch15t.py	15639	4f21e7bf37f83c7cdddfc2a92f85cf12	319
r2-ch15t.out	40945	d01c340f165f36d6cfaf5cef3ec87987	383
r2-ch15u.py	13977	6f181cd007fd063e0812e67505ed2cdd	299
r2-ch15u.out	21092	5cf78493cd6b4561675f8d5ad9f61a2e	292
READ-ch15n.md	10065	741e6a637196c4a55c6e01469cd53f7e	131
CENSUS-CLOSURES-ch15n.tsv	953	595c695e1020a6b320c60396656bcf82	4
r2-ch15v.py	11987	a46907c125ef47a47781d362f66bf639	245
r2-ch15v.out	9745	09da5878cb2dad5a5b08a92cd47da960	131
r2-ch15w.py	11709	c87fead9565448c6d577191b4e855f58	237
r2-ch15w.out	11655	912d5ef03d2694236d60e23504533547	150
READ-ch15o.md	10083	cfd5429052b11395bcc799ac6f6c1dc2	141
CENSUS-CLOSURES-ch15o.tsv	440	a1e9b6514dfb191bf9b758ffaaf68278	2
r2-ch15x.py	10174	ea1aa1aa4ee9d133aa692a546f1c425d	215
r2-ch15x.out	5809	5d649e632fec6600942a8233cdc559db	79
r2-ch15y.py	18484	5df14e7fa39073b97b0c837fdf000fcb	344
r2-ch15y.out	15592	76a751cdbe16e9c5a3e72a46fce9bc19	188
r2-ch15z.py	16734	d2fa71ce942d96e968715ac6179e77fe	350
r2-ch15z.out	18117	e0b5b5b2d3857b108b17c99a4466a4c0	241"""
ROWS = [(n, int(by), h, int(ln)) for n, by, h, ln in (l.split('\t') for l in ARCHIVE_MANIFEST.splitlines())]
NAMES = [n for n, _, _, _ in ROWS]
def block(name, body): return b'<<<FILE: ' + name.encode() + b'>>>\n' + body + b'<<<END FILE: ' + name.encode() + b'>>>\n'
def parse(t):
    ms = [(m.group(1).decode(), m.group(2), m.start(), m.end()) for m in MEMBER.finditer(t)]
    assert len(set(n for n, _, _, _ in ms)) == len(ms), 'duplicate member name'
    assert b'\n'.join(t[s:e] for _, _, s, e in ms) == t, 'bundle is not its blocks joined by one newline'
    return ms
def manifest_text(main_members, comp_members):   # close.py's format, verbatim in form
    rows = ['bundle\tname\tbytes\tmd5\tlines']
    for tag, ms in (('main', main_members), ('compendia', comp_members)):
        for n, b in sorted(ms):
            if n == 'MANIFEST.tsv': continue
            rows.append(f'{tag}\t{n}\t{len(b)}\t{md5(b)}\t{b.count(b"\n")}')
    return ('\n'.join(rows) + '\n').encode('utf-8')
def archive_manifest_text(ms):
    rows = ['bundle\tname\tbytes\tmd5\tlines'] + [f'archive\t{n}\t{len(b)}\t{md5(b)}\t{b.count(b"\n")}' for n, b in ms]
    return ('\n'.join(rows) + '\n').encode('utf-8')
def arg(k, default=None): return sys.argv[sys.argv.index(k) + 1] if k in sys.argv else default

def report():
    print('RULE:', ' | '.join(RULES))
    print(f'embedded archive manifest: {len(ROWS)} members  {sum(by for _, by, _, _ in ROWS):,} B  '
          f'{sum(ln for _, _, _, ln in ROWS):,} lines  md5(manifest text) {md5(ARCHIVE_MANIFEST.encode())}')
    assert all(is_arch(n) for n in NAMES), 'embedded name outside the rule'
    c = sorted(f for f in os.listdir(HOME) if re.match(r'The_Method_1_6_BUILD\d+_compendia', f))
    live = max(c, key=lambda f: int(re.search(r'BUILD(\d+)', f).group(1))) if c else None
    if live is None: print('live compendia bundle: none in /home/claude'); return
    ms = parse(open(os.path.join(HOME, live), 'rb').read()); ln = [n for n, _, _, _ in ms]
    present = [n for n in ln if n in NAMES]
    print(f'live bundle carries {len(present)} of the {len(NAMES)} archived names (expect 0 after the split)')
    union = set(ln) | set(NAMES); sel = {n for n in union if is_arch(n)}
    print(f'rule over (live names ∪ archived names) returns exactly the archived names: {sel == set(NAMES)}')
    assert sel == set(NAMES), f'rule drift: {sorted(sel ^ set(NAMES))[:10]}'

def verify_archive(p):
    ms = parse(open(p, 'rb').read()); d = {n: b for n, b, _, _ in ms}
    exp = dict((n, (by, h, ln)) for n, by, h, ln in ROWS); ok = 0
    for n, (by, h, ln) in exp.items():
        b = d.get(n)
        if b is None: print('FAIL absent', n); continue
        if (len(b), md5(b), b.count(b'\n')) != (by, h, ln): print('FAIL mismatch', n); continue
        ok += 1
    extra = set(d) - set(exp) - {'ARCHIVE-MANIFEST.tsv'}
    am = d.get('ARCHIVE-MANIFEST.tsv'); am_ok = am is not None and am == archive_manifest_text([(n, d[n]) for n in NAMES if n in d])
    print(f'archive {os.path.basename(p)}  {os.path.getsize(p):,} B  md5 {md5(open(p, "rb").read())}  {len(ms)} members; '
          f'{ok}/{len(exp)} verified; extra {sorted(extra)}; ARCHIVE-MANIFEST.tsv {"OK" if am_ok else "FAIL"}')
    return ok == len(exp) and not extra and am_ok

def split(old_p, out_a, out_l, main_p):
    assert not os.path.exists(out_a) and not os.path.exists(out_l), 'output exists — never overwrite'
    old = open(old_p, 'rb').read(); ms = parse(old)
    print(f'old {os.path.basename(old_p)}  {len(old):,} B  md5 {md5(old)}  {old.count(b"\n"):,} lines  {len(ms)} members')
    arch = [(i, n, b) for i, (n, b, _, _) in enumerate(ms) if is_arch(n)]
    live = [(i, n, b) for i, (n, b, _, _) in enumerate(ms) if not is_arch(n)]
    got = [(n, len(b), md5(b), b.count(b'\n')) for _, n, b in arch]
    assert got == ROWS, 'partition of OLD does not equal the embedded manifest'
    print(f'partition == embedded manifest: True  ({len(arch)} archive, {len(live)} live)')
    # (3) archive bundle
    a_ms = [(n, b) for _, n, b in arch]; am = archive_manifest_text(a_ms)
    archive = b'\n'.join([block(n, b) for n, b in a_ms] + [block('ARCHIVE-MANIFEST.tsv', am)])
    # (4) live bundle with rebuilt MANIFEST.tsv
    main_ms = [(n, b) for n, b, _, _ in parse(open(main_p, 'rb').read())]
    old_man = dict((n, b) for _, n, b in live)['MANIFEST.tsv']
    l_ms = [(n, b) for _, n, b in live]; new_man = manifest_text(main_ms, l_ms)
    l_ms2 = [(n, new_man if n == 'MANIFEST.tsv' else b) for n, b in l_ms]
    livebundle = b'\n'.join(block(n, b) for n, b in l_ms2)
    for tag, t in (('archive', archive), ('live', livebundle)):
        pm = parse(t); print(f'{tag} {os.path.basename(out_a if tag == "archive" else out_l)}  {len(t):,} B  md5 {md5(t)}  {t.count(b"\n"):,} lines  {len(pm)} members')
    print(f'MANIFEST.tsv (live)  {len(new_man):,} B  md5 {md5(new_man)}  {new_man.count(b"\n")} lines;  ARCHIVE-MANIFEST.tsv  {len(am):,} B  md5 {md5(am)}  {am.count(b"\n")} lines')
    # (5) reverse guard
    ra = parse(archive); assert ra[-1][0] == 'ARCHIVE-MANIFEST.tsv'; ra = ra[:-1]
    rl = parse(livebundle); rl = [(n, old_man if n == 'MANIFEST.tsv' else b) for n, b, _, _ in rl]
    idx = {}
    for (i, n, _), (rn, rb, _, _) in zip(arch, ra): assert n == rn; idx[i] = (n, rb)
    for (i, n, _), (rn, rb) in zip(live, rl): assert n == rn; idx[i] = (n, rb)
    rev = b'\n'.join(block(*idx[i]) for i in range(len(ms)))
    print(f'reverse recovers md5 {md5(rev)}  == old: {md5(rev) == md5(old)}')
    assert md5(rev) == md5(old), 'REVERSE GUARD FAILED — nothing written'
    open(out_a, 'wb').write(archive); open(out_l, 'wb').write(livebundle); print('written', out_a, 'and', out_l)

if __name__ == '__main__':
    if '--split' in sys.argv:
        report(); split(arg('--split'), arg('--archive'), arg('--live'), arg('--main', os.path.join(HOME, 'The_Method_1_6_BUILD90_main_and_register.md')))
    elif '--verify-archive' in sys.argv:
        report(); sys.exit(0 if verify_archive(arg('--verify-archive')) else 1)
    else:
        report()
