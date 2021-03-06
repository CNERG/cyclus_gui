"""
This file contains the templates class,
which is a collection of template strings.
"""

class template_collections:
    candu_template = """
     <facility>
    <!-- {{ country }} -->
    <!-- {{   type  }} -->
    <name>{{ reactor_name }}</name>
    <config>
      <Reactor>
        <fuel_inrecipes>  <val>natl_u_recipe</val>       </fuel_inrecipes>
        <fuel_outrecipes> <val>used_candu_recipe</val>  </fuel_outrecipes>
        <fuel_incommods>  <val>candu_fuel</val>                   </fuel_incommods>
        <fuel_outcommods> <val>used_candu</val>             </fuel_outcommods>
        <fuel_prefs>      <val>1.0</val>                   </fuel_prefs>
        <cycle_time>1</cycle_time>
        <refuel_time>0</refuel_time>
        <assem_size>{{assem_size}}</assem_size>
        <n_assem_core>{{ n_assem_core}}</n_assem_core>
        <n_assem_batch>{{n_assem_batch}}</n_assem_batch>
        <power_cap>{{capacity}}</power_cap>
      </Reactor>
    </config>
  </facility>
"""

    region_output_template = """
  <region>
      <name>{{country}}</name>
      <config><NullRegion/></config>
      <institution>
        <name>{{country_gov}}</name>
        <config>
          <DeployInst>

            {{ deployinst }}
            
          </DeployInst>
        </config>
      </institution>
  </region>
  """

    pwr_template_cyborg = """
    <facility>
    <!-- {{ country }} -->
    <!-- {{ type }}    -->
    <name>{{reactor_name}}</name>
    <config>
      <Cyborg>
        <power_cap>{{capacity}}</power_cap>
        <assem_size>{{assem_size}}</assem_size>
        <fuel_recipes>    <val>uox_fuel_recipe</val>      </fuel_recipes>
        <fuel_incommods>  <val>uox</val>           </fuel_incommods>
        <cycle_time>18</cycle_time>
        <refuel_time>2</refuel_time>
        <assembly_type>ce16x16</assembly_type>
        <fuel_type>UOX</fuel_type>
        <n_assem_core>{{n_assem_core}}</n_assem_core>
        <n_assem_batch>{{n_assem_batch}}</n_assem_batch>
        <spent_fuel>uox_waste</spent_fuel>
      </Cyborg>
    </config>
</facility>
"""

    pwr_template = """
     <facility>
    <!-- {{ country }} -->
    <!-- {{   type  }} -->
    <name>{{ reactor_name }}</name>
    <config>
      <Reactor>
        <fuel_inrecipes>  <val>uox_fuel_recipe</val>       </fuel_inrecipes>
        <fuel_outrecipes> <val>uox_used_fuel_recipe</val>  </fuel_outrecipes>
        <fuel_incommods>  <val>uox</val>                   </fuel_incommods>
        <fuel_outcommods> <val>uox_waste</val>             </fuel_outcommods>
        <fuel_prefs>      <val>1.0</val>                   </fuel_prefs>
        <cycle_time>18</cycle_time>
        <refuel_time>2</refuel_time>
        <assem_size>{{assem_size}}</assem_size>
        <n_assem_core>{{ n_assem_core}}</n_assem_core>
        <n_assem_batch>{{n_assem_batch}}</n_assem_batch>
        <power_cap>{{capacity}}</power_cap>
      </Reactor>
    </config>
  </facility>
"""

    smr_template = """
     <facility>
    <!-- {{ country }} -->
    <!-- {{   type  }} -->
    <name>{{ reactor_name }}</name>
    <config>
      <Reactor>
        <fuel_inrecipes>  <val>uox_fuel_recipe</val>       </fuel_inrecipes>
        <fuel_outrecipes> <val>uox_used_fuel_recipe</val>  </fuel_outrecipes>
        <fuel_incommods>  <val>uox</val>                   </fuel_incommods>
        <fuel_outcommods> <val>uox_waste</val>             </fuel_outcommods>
        <fuel_prefs>      <val>1.0</val>                   </fuel_prefs>
        <cycle_time>24</cycle_time>
        <refuel_time>2</refuel_time>
        <assem_size>{{assem_size}}</assem_size>
        <n_assem_core>{{ n_assem_core}}</n_assem_core>
        <n_assem_batch>{{n_assem_batch}}</n_assem_batch>
        <power_cap>{{capacity}}</power_cap>
      </Reactor>
    </config>
  </facility>
"""

    smr_template_cyborg = """
    <facility>
    <!-- {{ country }} -->
    <!-- {{ type }}    -->
    <name>{{reactor_name}}</name>
    <config>
      <Cyborg>
        <power_cap>{{capacity}}</power_cap>
        <assem_size>{{assem_size}}</assem_size>
        <fuel_recipes>    <val>uox_fuel_recipe</val>      </fuel_recipes>
        <fuel_incommods>  <val>uox</val>           </fuel_incommods>
        <cycle_time>24</cycle_time>
        <refuel_time>2</refuel_time>
        <assembly_type>ce16x16</assembly_type>
        <fuel_type>UOX</fuel_type>
        <n_assem_core>{{n_assem_core}}</n_assem_core>
        <n_assem_batch>{{n_assem_batch}}</n_assem_batch>
        <spent_fuel>uox_waste</spent_fuel>
      </Cyborg>
    </config>
</facility>
"""

    mox_template_cyborg = """
     <facility>
    <!-- {{ country }} -->
    <!-- {{   type  }} -->
    <name>{{ reactor_name }}</name>
    <config>
      <Cyborg>
        <power_cap>{{capacity}}</power_cap>
        <assem_size>{{assem_size}}</assem_size>
        <fuel_recipes>  <val>uox_fuel_recipe</val>       <val>mox_fuel_recipe</val>        </fuel_inrecipes>
        <fuel_incommods>  <val>uox</val>                   <val>mox</val>                    </fuel_incommods>
        <fuel_prefs>      <val>1.0</val>                   <val>2.0</val>                    </fuel_prefs>
        <cycle_time>18</cycle_time>
        <refuel_time>2</refuel_time>
        <assembly_type>mox_ce16x16</assembly_type>
        <fuel_type>MOX</fuel_type>
        <n_assem_core>{{ n_assem_core}}</n_assem_core>
        <n_assem_batch>{{n_assem_batch}}</n_assem_batch>
        <spent_fuel>spent_fuel</spent_fuel>
      </Cyborg>
    </config>
</facility>
"""

    mox_template = """
     <facility>
    <!-- {{ country }} -->
    <!-- {{   type  }} -->
    <name>{{ reactor_name }}</name>
    <config>
      <Reactor>
        <fuel_inrecipes>  <val>uox_fuel_recipe</val>       <val>mox_fuel_recipe</val>        </fuel_inrecipes>
        <fuel_outrecipes> <val>uox_used_fuel_recipe</val>  <val>mox_used_fuel_recipe</val>   </fuel_outrecipes>
        <fuel_incommods>  <val>uox</val>                   <val>mox</val>                    </fuel_incommods>
        <fuel_outcommods> <val>uox_waste</val>             <val>mox_waste</val>              </fuel_outcommods>
        <fuel_prefs>      <val>1.0</val>                   <val>2.0</val>                    </fuel_prefs>
        <cycle_time>18</cycle_time>
        <refuel_time>2</refuel_time>
        <assem_size>{{assem_size}}</assem_size>
        <n_assem_core>{{ n_assem_core}}</n_assem_core>
        <n_assem_batch>{{n_assem_batch}}</n_assem_batch>
        <power_cap>{{capacity}}</power_cap>
      </Reactor>
    </config>
  </facility>
"""

    magnox_template = """
     <facility>
    <!-- {{ country }} -->
    <!-- {{   type  }} -->
    <name>{{ reactor_name }}</name>
    <config>
      <Reactor>
        <fuel_inrecipes>  <val>nat_u_recipe</val>   </fuel_inrecipes>
        <fuel_outrecipes> <val>magnox_used</val>    </fuel_outrecipes>
        <fuel_incommods>  <val>nat_u</val>          </fuel_incommods>
        <fuel_outcommods> <val>magnox_waste</val>   </fuel_outcommods>
        <fuel_prefs>      <val>1.0</val>            </fuel_prefs>
        <cycle_time>18</cycle_time>
        <refuel_time>2</refuel_time>
        <assem_size>{{assem_size}}</assem_size>
        <n_assem_core>{{ n_assem_core}}</n_assem_core>
        <n_assem_batch>{{n_assem_batch}}</n_assem_batch>
        <power_cap>{{capacity}}</power_cap>
      </Reactor>
    </config>
  </facility>
"""

    input_template = """

<simulation>
  <control>
    <duration>{{duration}}</duration>
    <startmonth>{{ startmonth}}</startmonth>
    <startyear>{{ startyear}}</startyear>
    <decay>lazy</decay>
  </control>

  <archetypes>
    <spec>
      <lib>cycamore</lib>
      <name>Source</name>
    </spec>
    <spec>
      <lib>cycamore</lib>
      <name>Storage</name>
    </spec>
    <spec>
      <lib>cycamore</lib>
      <name>Sink</name>
    </spec>
    <spec>
        <lib>cycamore</lib>
        <name>Reactor</name>
    </spec>
    <spec>
      <lib>agents</lib>
      <name>NullRegion</name>
    </spec>
    <spec>
      <lib>agents</lib>
      <name>NullInst</name>
    </spec>
    <spec>
      <lib>cycamore</lib>
      <name>Separations</name>
    </spec>
    <spec>
      <lib>cycamore</lib>
      <name>DeployInst</name>
    </spec>
    <spec>
      <lib>cycamore</lib>
      <name>Enrichment</name>
    </spec>
    <spec>
      <lib>cycamore</lib>
      <name>Mixer</name>
    </spec>
  </archetypes>


<facility>
    <name>mixer</name>
    <config>
      <Mixer>
        <in_streams>
          <stream>
            <info>
              <mixing_ratio>.09</mixing_ratio>
              <buf_size>1e+299</buf_size>
            </info>
            <commodities>
              <item>
                <commodity>Pu</commodity>
                <pref>1.0</pref>
              </item>
            </commodities>
          </stream>
          <stream>
            <info>
              <mixing_ratio>.91</mixing_ratio>
              <buf_size>1e+299</buf_size>
            </info>
            <commodities>
              <item>
                <commodity>tailings</commodity>
                <pref>1.0</pref>
              </item>
            </commodities>
          </stream>
        </in_streams>
        <out_commod>mox</out_commod>
        <out_buf_size>1e+299</out_buf_size>
        <throughput>1e+299</throughput>
      </Mixer>
    </config>
</facility>


<!-- La Hague Model from Schneider & Marignac -->
  <facility>
    <name>reprocessing</name>
    <config>
      <Separations>
         <feed_commods>   <val>uox_waste</val> </feed_commods>
         <feed_commod_prefs> <val>1.0</val> </feed_commod_prefs>
         <feed_recipe>uox_used_fuel_recipe</feed_recipe>
         <feedbuf_size>1e299</feedbuf_size>
         <throughput>1e299</throughput>
         <leftover_commod>reprocess_waste</leftover_commod>
         <leftoverbuf_size>1e100</leftoverbuf_size>
         <streams>
          <item>
            <commod>pu</commod>
            <info>
              <buf_size>1e299</buf_size>
              <efficiencies>
                <item>
                  <comp>Pu</comp> <eff>.99</eff>
                </item>
                </efficiencies>
            </info>
          </item>
          <item>
            <commod>u</commod>
            <info>
              <buf_size>1e299</buf_size>
              <efficiencies>
                <item>
                  <comp>U</comp> <eff>.99</eff>
                </item>
                </efficiencies>
            </info>
          </item>
        </streams>
      </Separations>
    </config>
  </facility>

  <facility>
    <name>enrichment</name>
    <config>
      <Enrichment>
        <feed_commod>natl_u</feed_commod>
        <feed_recipe>natl_u_recipe</feed_recipe>
        <product_commod>uox</product_commod>
        <tails_assay>0.003</tails_assay>
        <tails_commod>tailings</tails_commod>
        <swu_capacity>1e100</swu_capacity>
        <initial_feed>1e100</initial_feed>
      </Enrichment>
    </config>
  </facility>

  <facility>
    <name>nat_u_source</name>
    <config>
      <Source>
        <outcommod>natl_u</outcommod>
        <outrecipe>natl_u_recipe</outrecipe>
        <throughput>1e100</throughput>
      </Source>
    </config>
  </facility>

  <facility>
    <name>SomeSink</name>
    <config>
      <Sink>
        <in_commods>
          <val>uox_waste</val>
          <val>used_candu</val>
          <val>mox_waste</val>
          <val>used_candu</val>
          <val>tailings</val>
          <val>reprocess_waste</val>
        </in_commods>
        <capacity>1e100</capacity>
      </Sink>
    </config>
  </facility>

{{reactor_input}}

{{ region_input }}
  
<region>
    <name>RandLand</name>
    <config><NullRegion/></config>
        <institution>  
         <name>Fuel_Cycle_Facilities</name>
         <config><NullInst/></config>
        <initialfacilitylist>
          <entry>
            <number>1</number>
            <prototype>nat_u_source</prototype>
          </entry>
          <entry>
            <number>1</number>
            <prototype>enrichment</prototype>
          </entry>
          <entry>
            <number>1</number>
            <prototype>SomeSink</prototype>
          </entry>
          <entry>
            <number>1</number>
            <prototype>mixer</prototype>
          </entry>
          {{reprocessing}}
        </initialfacilitylist>
        </institution>
</region>  

  <recipe>
    <name>natl_u_recipe</name>
    <basis>mass</basis>
    <nuclide> <id>U235</id> <comp>0.711</comp> </nuclide>
    <nuclide> <id>U238</id> <comp>99.289</comp> </nuclide>
  </recipe>

  <recipe>
    <name>uox_fuel_recipe</name>
    <basis>mass</basis>
     <nuclide> <id>U234</id>  <comp>0.0002558883</comp> </nuclide> 
     <nuclide> <id>U235</id>  <comp>0.0319885317</comp> </nuclide> 
     <nuclide> <id>U238</id>  <comp>0.96775558</comp> </nuclide> 
  </recipe> 

  <recipe>
    <name>depleted_u</name>
    <basis>mass</basis>
    <nuclide> <id>U235</id><comp>0.003</comp></nuclide>
    <nuclide><id>U238</id><comp>0.997</comp></nuclide>
  </recipe>


  <recipe>
    <name>mox_fuel_recipe</name>
    <basis>mass</basis>
     <nuclide> <id>U232</id>  <comp>1.2872E-10</comp> </nuclide> 
     <nuclide> <id>U233</id>  <comp>1.38E-09</comp> </nuclide> 
     <nuclide> <id>U234</id>  <comp>.000143528</comp> </nuclide> 
     <nuclide> <id>U235</id>  <comp>.007420728</comp> </nuclide> 
     <nuclide> <id>U236</id>  <comp>.003556698</comp> </nuclide>
     <nuclide> <id>U237</id>  <comp>3.34366E-11</comp> </nuclide>  
     <nuclide> <id>U238</id>  <comp>0.868879045</comp> </nuclide>
     <nuclide> <id>U239</id>  <comp>2.26477E-19</comp> </nuclide> 
     <nuclide> <id>Pu238</id>  <comp>0.001440424</comp> </nuclide> 
     <nuclide> <id>Pu239</id>  <comp>0.066449749</comp> </nuclide> 
     <nuclide> <id>Pu240</id>  <comp>0.029770312</comp> </nuclide> 
     <nuclide> <id>Pu241</id>  <comp>0.016094726</comp> </nuclide> 
     <nuclide> <id>Pu242</id>  <comp>0.006244625</comp> </nuclide>
     <nuclide> <id>Pu243</id>  <comp>3.95537E-19</comp> </nuclide> 
     <nuclide> <id>Pu244</id>  <comp>1.64638E-07</comp> </nuclide> 
     <nuclide> <id>Pu245</id>  <comp>1.43248E-24</comp> </nuclide> 
  </recipe> 

   <recipe>
    <name>mox_used_fuel_recipe</name>
    <basis>mass</basis>
     <nuclide> <id>He4</id>  <comp>2.51087058608741E-05</comp> </nuclide> 
     <nuclide> <id>Ra226</id>  <comp>6.85864649540962E-14</comp> </nuclide> 
     <nuclide> <id>Ra228</id>  <comp>1.0769444927185E-19</comp> </nuclide> 
     <nuclide> <id>Pb206</id>  <comp>3.63781250186619E-18</comp> </nuclide> 
     <nuclide> <id>Pb207</id>  <comp>1.05894542041679E-15</comp> </nuclide> 
     <nuclide> <id>Pb208</id>  <comp>2.00189681933373E-12</comp> </nuclide> 
     <nuclide> <id>Pb210</id>  <comp>1.1829390296063E-19</comp> </nuclide> 
     <nuclide> <id>Th228</id>  <comp>4.90174735683015E-12</comp> </nuclide> 
     <nuclide> <id>Th229</id>  <comp>1.43792588721374E-12</comp> </nuclide> 
     <nuclide> <id>Th230</id>  <comp>2.39987630689358E-09</comp> </nuclide> 
     <nuclide> <id>Th232</id>  <comp>8.76554821092882E-10</comp> </nuclide> 
     <nuclide> <id>Bi209</id>  <comp>2.68786146372081E-16</comp> </nuclide> 
     <nuclide> <id>Ac227</id>  <comp>2.46087316302713E-14</comp> </nuclide> 
     <nuclide> <id>Pa231</id>  <comp>7.06963562072402E-10</comp> </nuclide> 
     <nuclide> <id>U232</id>  <comp>5.93369416879439E-10</comp> </nuclide> 
     <nuclide> <id>U233</id>  <comp>1.03594660580906E-08</comp> </nuclide> 
     <nuclide> <id>U234</id>  <comp>0.0002656863</comp> </nuclide> 
     <nuclide> <id>U235</id>  <comp>0.0043397763</comp> </nuclide> 
     <nuclide> <id>U236</id>  <comp>0.0051097366</comp> </nuclide> 
     <nuclide> <id>U238</id>  <comp>0.8283573053</comp> </nuclide> 
     <nuclide> <id>Np237</id>  <comp>0.0043297768</comp> </nuclide> 
     <nuclide> <id>Pu238</id>  <comp>0.0060396887</comp> </nuclide> 
     <nuclide> <id>Pu239</id>  <comp>0.0410078864</comp> </nuclide> 
     <nuclide> <id>Pu240</id>  <comp>0.0283985363</comp> </nuclide> 
     <nuclide> <id>Pu241</id>  <comp>0.0146892429</comp> </nuclide> 
     <nuclide> <id>Pu242</id>  <comp>0.0098784908</comp> </nuclide> 
     <nuclide> <id>Pu244</id>  <comp>2.18888718157919E-07</comp> </nuclide> 
     <nuclide> <id>Am241</id>  <comp>0.0021278903</comp> </nuclide> 
     <nuclide> <id>Am242m</id>  <comp>5.0357404506317E-05</comp> </nuclide> 
     <nuclide> <id>Am243</id>  <comp>0.0020828926</comp> </nuclide> 
     <nuclide> <id>Cm242</id>  <comp>0.0002752858</comp> </nuclide> 
     <nuclide> <id>Cm243</id>  <comp>1.26393485496395E-05</comp> </nuclide> 
     <nuclide> <id>Cm244</id>  <comp>0.0010179475</comp> </nuclide> 
     <nuclide> <id>Cm245</id>  <comp>0.0001275934</comp> </nuclide> 
     <nuclide> <id>Cm246</id>  <comp>6.14068350026396E-06</comp> </nuclide> 
     <nuclide> <id>Cm247</id>  <comp>1.20593784421403E-07</comp> </nuclide> 
     <nuclide> <id>Cm248</id>  <comp>9.15852795618264E-09</comp> </nuclide> 
     <nuclide> <id>Cm250</id>  <comp>3.73380755414193E-17</comp> </nuclide> 
     <nuclide> <id>Cf249</id>  <comp>4.05679090711136E-11</comp> </nuclide> 
     <nuclide> <id>Cf250</id>  <comp>2.9328488367162E-11</comp> </nuclide> 
     <nuclide> <id>Cf251</id>  <comp>1.4479253718258E-11</comp> </nuclide> 
     <nuclide> <id>Cf252</id>  <comp>7.53461165518465E-12</comp> </nuclide> 
     <nuclide> <id>H3</id>  <comp>1.02694706965821E-07</comp> </nuclide> 
     <nuclide> <id>C14</id>  <comp>3.95879595791321E-11</comp> </nuclide> 
     <nuclide> <id>Kr81</id>  <comp>7.34462144755557E-11</comp> </nuclide> 
     <nuclide> <id>Kr85</id>  <comp>2.05489408777763E-05</comp> </nuclide> 
     <nuclide> <id>Sr90</id>  <comp>0.000408279</comp> </nuclide> 
     <nuclide> <id>Tc99</id>  <comp>0.0011189423</comp> </nuclide> 
     <nuclide> <id>I129</id>  <comp>0.0003505819</comp> </nuclide> 
     <nuclide> <id>Cs134</id>  <comp>0.0002101892</comp> </nuclide> 
     <nuclide> <id>Cs135</id>  <comp>0.0009355518</comp> </nuclide> 
     <nuclide> <id>Cs137</id>  <comp>0.0018309056</comp> </nuclide> 
  </recipe> 

  <recipe>
    <name>uox_used_fuel_recipe</name>
    <basis>mass</basis>
     <nuclide> <id>He4</id>  <comp>2.09687731425456E-07</comp> </nuclide> 
     <nuclide> <id>Ra226</id>  <comp>1.18893043712383E-14</comp> </nuclide> 
     <nuclide> <id>Ra228</id>  <comp>6.05164592554536E-21</comp> </nuclide> 
     <nuclide> <id>Pb206</id>  <comp>7.66855132237399E-20</comp> </nuclide> 
     <nuclide> <id>Pb207</id>  <comp>6.51861860354101E-17</comp> </nuclide> 
     <nuclide> <id>Pb208</id>  <comp>1.2309279798986E-13</comp> </nuclide> 
     <nuclide> <id>Pb210</id>  <comp>2.49685391210951E-20</comp> </nuclide> 
     <nuclide> <id>Th228</id>  <comp>6.56361597079969E-13</comp> </nuclide> 
     <nuclide> <id>Th229</id>  <comp>1.70690013134599E-13</comp> </nuclide> 
     <nuclide> <id>Th230</id>  <comp>0.000000001</comp> </nuclide> 
     <nuclide> <id>Th232</id>  <comp>1.56490843910748E-10</comp> </nuclide> 
     <nuclide> <id>Bi209</id>  <comp>2.5848487636376E-17</comp> </nuclide> 
     <nuclide> <id>Ac227</id>  <comp>3.45679774696139E-15</comp> </nuclide> 
     <nuclide> <id>Pa231</id>  <comp>2.25186824592336E-10</comp> </nuclide> 
     <nuclide> <id>U232</id>  <comp>1.39991809249232E-10</comp> </nuclide> 
     <nuclide> <id>U233</id>  <comp>1.31692294843742E-09</comp> </nuclide> 
     <nuclide> <id>U234</id>  <comp>0.0001558909</comp> </nuclide> 
     <nuclide> <id>U235</id>  <comp>0.0080635282</comp> </nuclide> 
     <nuclide> <id>U236</id>  <comp>0.0038647739</comp> </nuclide> 
     <nuclide> <id>U238</id>  <comp>0.9441447592</comp> </nuclide> 
     <nuclide> <id>Np237</id>  <comp>0.0003316806</comp> </nuclide> 
     <nuclide> <id>Pu238</id>  <comp>0.0001076937</comp> </nuclide> 
     <nuclide> <id>Pu239</id>  <comp>0.0050287058</comp> </nuclide> 
     <nuclide> <id>Pu240</id>  <comp>0.0022528682</comp> </nuclide> 
     <nuclide> <id>Pu241</id>  <comp>0.0012229284</comp> </nuclide> 
     <nuclide> <id>Pu242</id>  <comp>0.0004725724</comp> </nuclide> 
     <nuclide> <id>Pu244</id>  <comp>1.24592710231816E-08</comp> </nuclide> 
     <nuclide> <id>Am241</id>  <comp>2.97982565401936E-05</comp> </nuclide> 
     <nuclide> <id>Am242m</id>  <comp>3.55779183791976E-07</comp> </nuclide> 
     <nuclide> <id>Am243</id>  <comp>7.89053833418348E-05</comp> </nuclide> 
     <nuclide> <id>Cm242</id>  <comp>1.15793225079007E-05</comp> </nuclide> 
     <nuclide> <id>Cm243</id>  <comp>0.00000024</comp> </nuclide> 
     <nuclide> <id>Cm244</id>  <comp>2.20987070314859E-05</comp> </nuclide> 
     <nuclide> <id>Cm245</id>  <comp>1.02693991499258E-06</comp> </nuclide> 
     <nuclide> <id>Cm246</id>  <comp>9.56844016218499E-08</comp> </nuclide> 
     <nuclide> <id>Cm247</id>  <comp>8.39550878897535E-10</comp> </nuclide> 
     <nuclide> <id>Cm248</id>  <comp>4.3267468472959E-11</comp> </nuclide> 
     <nuclide> <id>Cm250</id>  <comp>1.99688316479083E-19</comp> </nuclide> 
     <nuclide> <id>Cf249</id>  <comp>4.3937429274366E-14</comp> </nuclide> 
     <nuclide> <id>Cf250</id>  <comp>8.11752505346616E-14</comp> </nuclide> 
     <nuclide> <id>Cf251</id>  <comp>3.16081506454872E-14</comp> </nuclide> 
     <nuclide> <id>Cf252</id>  <comp>1.66790241305513E-14</comp> </nuclide> 
     <nuclide> <id>H3</id>  <comp>5.74866365267024E-08</comp> </nuclide> 
     <nuclide> <id>C14</id>  <comp>2.63084607239092E-11</comp> </nuclide> 
     <nuclide> <id>Kr81</id>  <comp>2.16087356991135E-11</comp> </nuclide> 
     <nuclide> <id>Kr85</id>  <comp>2.41685859253852E-05</comp> </nuclide> 
     <nuclide> <id>Sr90</id>  <comp>0.0005372686</comp> </nuclide> 
     <nuclide> <id>Tc99</id>  <comp>0.0007822542</comp> </nuclide> 
     <nuclide> <id>I129</id>  <comp>0.0001810894</comp> </nuclide> 
     <nuclide> <id>Cs134</id>  <comp>0.0001230928</comp> </nuclide> 
     <nuclide> <id>Cs135</id>  <comp>0.0003052821</comp> </nuclide> 
     <nuclide> <id>Cs137</id>  <comp>0.0012009297</comp> </nuclide> 

  </recipe> 

</simulation>
"""

    deployinst_template = """
    <prototypes>
    {{ prototype }}
</prototypes>
<build_times>
    {{ start_time }}
</build_times>
<n_build>
    {{ number }}
</n_build>
<lifetimes>
    {{ lifetime }}
</lifetimes>
"""

    candu_template_cyborg = """
    <facility>
    <!-- {{ country }} -->
    <!-- {{ type }}    -->
    <name>{{reactor_name}}</name>
    <config>
      <Cyborg>
        <power_cap>{{capacity}}</power_cap>
        <assem_size>{{assem_size}}</assem_size>
        <fuel_recipes>    <val>natl_u_recipe</val>      </fuel_recipes>
        <fuel_incommods>  <val>natl_u</val>           </fuel_incommods>
        <cycle_time>1</cycle_time>
        <refuel_time>0</refuel_time>
        <assembly_type>candu19</assembly_type>
        <fuel_type>UOX</fuel_type>
        <n_assem_core>{{n_assem_core}}</n_assem_core>
        <n_assem_batch>{{n_assem_batch}}</n_assem_batch>
        <spent_fuel>used_candu</spent_fuel>
      </Cyborg>
    </config>
</facility>
"""
